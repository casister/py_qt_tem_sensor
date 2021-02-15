
/***************************** Include Files *********************************/

#include "xparameters.h"
#include "xscugic.h"
#include "xil_exception.h"
#include <stdio.h>
#include <stdlib.h>
#include "xspi.h"		/* SPI device driver */
#include "math.h"
#include "platform.h"
#include "xgpio.h"

// 0x80 MAX31723 Conf. Register Address
#define MAX31723_CONFIG_REG_ADDRESS   0x80
#define MAX31723_TEMP_LSB_REG_ADDRESS 0x01
#define MAX31723_TEMP_MSB_REG_ADDRESS 0x02

// Bits 0-1-2 define ADC resolution
#define MAX31723_THERMOMETER_RESOLUTION_9BIT_MODE  0x00
#define MAX31723_THERMOMETER_RESOLUTION_10BIT_MODE 0x02
#define MAX31723_THERMOMETER_RESOLUTION_11BIT_MODE 0x04
#define MAX31723_THERMOMETER_RESOLUTION_12BIT_MODE 0x06

#define MAX31723_CONTINUOUS_TEMPERATURE_CONVERSION_MODE 0x00  //bit 4
#define MAX31723_COMPARATOR_MODE 0x00                         //bit 3
#define MAX31723_DISABLE_ONE_SHOT_TEMPERATURE_CONVERSION 0x00 //bit 4

// Define the temperature calibration offset here
#define TEMPERATURE_CALIBRATION_OFFSET -3.30

//This is the size of the buffer to be transmitted/received
#define BUFFER_SIZE 4

XGpio GpioInstance;
static XSpi SpiInstance;	 /* The instance of the SPI device */


/**************************** Type Definitions *******************************/
/*
 * The following data type is used to send and receive data on the SPI
 * interface.
 */
typedef u8 DataBuffer[BUFFER_SIZE];

/************************** Function Prototypes ******************************/

void SpiIntrHandler(void *CallBackRef, u32 StatusEvent, u32 ByteCount);
void display_buffers(void);
void clear_SPI_buffers(void);
float read_current_temperature(XSpi *SpiInstance);


/************************** Variable Definitions *****************************/


/*
 * The following variables are shared between non-interrupt processing and
 * interrupt processing such that they must be global.
 */
volatile int SPI_TransferInProgress;
int SPI_Error_Count;


/*
 * The following variables are used to read and write to the  Spi device, they
 * are global to avoid having large buffers on the stack.
 */
u8 ReadBuffer[BUFFER_SIZE];
u8 WriteBuffer[BUFFER_SIZE];

// commands to execute: Python App send them
// 7 = to the amount of chars that make the string to decode
int command2execute(){
	char command[7];
	scanf("%7s", command);
	if(strcmp(command, "rd_temp") == 0){   //read temperature gd
		return 1;
	}else if(strcmp(command, "wr_leds") == 0){ //write GPIO LEDs
		return 2;
	}else{
		return 0;
	}

}

// get 3 char from the Python code, and convert them into
// one integer -atoi-. The integer is then ent to the LEDs using
// XGpio_DiscreteWrite
void set_gpios(){
	char state[3];
	scanf("%3s", state);
	XGpio_DiscreteWrite(&GpioInstance, 1, atoi(state));
}

void send_temperature(){
	float temperature = read_current_temperature(&SpiInstance);
	printf("%2.4f", temperature);		// sensor 1
	printf("%2.4f", temperature+0.01);	// sensor 2
	printf("%2.4f", temperature+0.02);	// sensor 3
	printf("%2.4f", temperature+0.03);	// sensor 4
	printf("%2.4f", temperature+0.04);	// sensor 5
	printf("%2.4f", temperature+0.05);	// sensor 6
	printf("%2.4f", temperature+0.06);	// sensor 7
	printf("%2.4f", temperature+0.07);	// sensor 8
	printf("%2.4f", temperature+0.08);	// sensor 9
	printf("%2.4f", temperature-0.01);	// sensor 10
	printf("%2.4f", temperature-0.02);	// sensor 11
	printf("%2.4f", temperature-0.03);	// sensor 12
	printf("%2.4f", temperature-0.04);	// sensor 13
	printf("%2.4f", temperature-0.05);	// sensor 14
	printf("%2.4f", temperature-0.06);	// sensor 15
	printf("%2.4f", temperature-0.07);	// sensor 16


}

int main(void)
{
	WriteBuffer[0]=0x55;
	WriteBuffer[1]=0xaa;

	init_platform();

	// ------- Interrupt related declarations
	XScuGic_Config *IntcConfig;
	XScuGic IntcInstance;		 /* Interrupt Controller Instance */
	// ------- SPI related declarations
	XSpi_Config *SPI_ConfigPtr;



	XGpio_Initialize(&GpioInstance, XPAR_AXI_GPIO_0_DEVICE_ID);
	XGpio_SetDataDirection(&GpioInstance, 1, 0);

	int Status;
    // ------------------- SPI related functions --------------------- //
	// Initialize the SPI driver
	SPI_ConfigPtr = XSpi_LookupConfig(XPAR_AXI_QUAD_SPI_0_DEVICE_ID);
	if (SPI_ConfigPtr == NULL) return XST_DEVICE_NOT_FOUND;

	Status = XSpi_CfgInitialize(&SpiInstance, SPI_ConfigPtr, SPI_ConfigPtr->BaseAddress);
	if (Status != XST_SUCCESS) return XST_FAILURE;

	// Reset the SPI peripheral
	XSpi_Reset(&SpiInstance);

	// Perform a self-test to ensure that the SPI hardware was built correctly.
	Status = XSpi_SelfTest(&SpiInstance);
	if (Status != XST_SUCCESS) return XST_FAILURE;

	//printf("MAX31723PMB1 PMOD test\n\r\n\r");

	// Run loopback test only in case of standard SPI mode.
	if (SpiInstance.SpiMode != XSP_STANDARD_MODE) return XST_SUCCESS;

	// --------------- Interrupt (GIC) related functions ------------ //
	// Initialize the Interrupt controller so that it is ready to use.
	IntcConfig = XScuGic_LookupConfig(XPAR_SCUGIC_0_DEVICE_ID);
	if (NULL == IntcConfig) return XST_FAILURE;

	Status = XScuGic_CfgInitialize(&IntcInstance, IntcConfig, IntcConfig->CpuBaseAddress);
	if (Status != XST_SUCCESS) return XST_FAILURE;

	//cs!!
	XScuGic_SetPriorityTriggerType(&IntcInstance, XPAR_FABRIC_AXI_QUAD_SPI_0_IP2INTC_IRPT_INTR, 0xA0, 0x3);

	// Connect a device driver handler that will be called when an interrupt
	// for the device occurs, the device driver handler performs the
	// specific interrupt processing for the device.
	// >> Note: Definitions for Fabric interrupts connected to ps7_scugic_0
    // #define XPAR_FABRIC_AXI_QUAD_SPI_0_IP2INTC_IRPT_INTR 61 << End Note
	Status = XScuGic_Connect(&IntcInstance, XPAR_FABRIC_AXI_QUAD_SPI_0_IP2INTC_IRPT_INTR, (Xil_ExceptionHandler)XSpi_InterruptHandler, (void *)&SpiInstance);
	if (Status != XST_SUCCESS) return Status;

	// Enable the interrupt for the SPI peripheral.
	XScuGic_Enable(&IntcInstance, XPAR_FABRIC_AXI_QUAD_SPI_0_IP2INTC_IRPT_INTR);

	// Initialize exceptions on the ARM processor
	Xil_ExceptionInit();

	// Connect the interrupt controller interrupt handler to the hardware interrupt handling logic in the processor.
	Xil_ExceptionRegisterHandler(XIL_EXCEPTION_ID_IRQ_INT, (Xil_ExceptionHandler)XScuGic_InterruptHandler, &IntcInstance);

	// Enable interrupts in the Processor.
	Xil_ExceptionEnable();

	// Setup the handler for the SPI that will be called from the interrupt
	// context when an SPI status occurs, specify a pointer to the SPI
	// driver instance as the callback reference so the handler is able to
	// access the instance data.
	XSpi_SetStatusHandler(&SpiInstance, &SpiInstance, (XSpi_StatusHandler)SpiIntrHandler);

	// Set the SPI device to the correct mode for this application
	//printf("Setting the SPI device into Master mode...");
	Status = XSpi_SetOptions(&SpiInstance, XSP_MASTER_OPTION + XSP_MANUAL_SSELECT_OPTION + XSP_CLK_PHASE_1_OPTION);
	if (Status != XST_SUCCESS) return XST_FAILURE;
	//printf("DONE!!\n\r");

	// Select the SPI Slave.  This asserts the correct SS bit on the SPI bus
	XSpi_SetSlaveSelect(&SpiInstance, 0x01);

	// Start the SPI driver so that interrupts and the device are enabled.
	//printf("Starting the SPI driver, enabling interrupts and the device...");
	XSpi_Start(&SpiInstance);
	//printf("DONE!!\n\r");

	//printf("\n\r\n\r");
	//printf("Writing to the MAX31723 Config Register...");

	// Clear the SPI read and write buffers
	clear_SPI_buffers();

	// Put the commands for the MAX31723 device in the write buffer
	// See Table 3 of MAX31723 Datasheet
	WriteBuffer[0] = MAX31723_CONFIG_REG_ADDRESS;                       //Configuration Register Address
	WriteBuffer[1] = MAX31723_DISABLE_ONE_SHOT_TEMPERATURE_CONVERSION + // bit 4 = 0
			 	 	 MAX31723_COMPARATOR_MODE +                         // bit 3 = 0
					 MAX31723_THERMOMETER_RESOLUTION_12BIT_MODE +       // bits 2:1 = 1 (12 bits)
					 MAX31723_CONTINUOUS_TEMPERATURE_CONVERSION_MODE;   //

	// Transmit the data to write the Configuration Register
	SPI_TransferInProgress = TRUE;
	Status = XSpi_Transfer(&SpiInstance, WriteBuffer, NULL, 2);

	while (SPI_TransferInProgress);  // Wait here until the SPI transfer has finished
	//printf("DONE!\n\r\n\r\n\r");

	// An endless loop which reads and displays the current temperature
	while(1)
	{
		int result = command2execute();
		switch(result){
		case 1:
			send_temperature();
			break;
		case 2:
			set_gpios();
			break;
		}
	}


	// Disable and disconnect the interrupt system.
	XScuGic_Disconnect(&IntcInstance, XPAR_FABRIC_AXI_QUAD_SPI_0_IP2INTC_IRPT_INTR);

    cleanup_platform();

	return XST_SUCCESS;
}



void SpiIntrHandler(void *CallBackRef, u32 StatusEvent, u32 ByteCount)
{
	//printf("** In the SPI Interrupt handler **\n\r");
	//printf("Number of bytes transferred, as seen by the handler = %d\n\r", ByteCount);

	// Indicate the transfer on the SPI bus is no longer in progress
	// regardless of the status event.
	if (StatusEvent == XST_SPI_TRANSFER_DONE)
	{
		SPI_TransferInProgress = FALSE;
		//printf("Interrupt Handler\n\r");//cs
	}
	else	// If the event was not transfer done, then track it as an error.
	{
		printf("\n\r\n\r ** SPI ERROR **\n\r\n\r");
		SPI_Error_Count++;
	}
}



void clear_SPI_buffers(void)
{
	int SPI_Count;

	// Initialize the write buffer and read buffer to zero
	for (SPI_Count = 0; SPI_Count < BUFFER_SIZE; SPI_Count++)
	{
		WriteBuffer[SPI_Count] = 0;
		ReadBuffer[SPI_Count] = 0;
	}
}

float read_current_temperature(XSpi *SpiInstance)
{
	u8 Temperature_LSB = 0;
	u8 Temperature_MSB = 0;
	float Temperature_LSB_float = 0;
	float Temperature_MSB_float = 0;
	float Temperature_float = 0;
	int Status = 0;
	int i = 0;

	//cs
	Temperature_MSB = 0xAA;
	Temperature_LSB = 0x55;

	// Clear the SPI read and write buffers
	clear_SPI_buffers();

	// Put the commands for the MAX31723 device in the write buffer
	WriteBuffer[0] = MAX31723_TEMP_MSB_REG_ADDRESS;//[0]
	WriteBuffer[1] = 0x00000000;//[1]

	// Transmit the data.
	SPI_TransferInProgress = TRUE;
	Status = XSpi_Transfer(SpiInstance, WriteBuffer, ReadBuffer, 2);

	while (SPI_TransferInProgress);  // Wait here until the SPI transfer has finished

	// Fetch the byte of data from the ReadBuffer
	Temperature_MSB = ReadBuffer[1];//cs[1]

	// Clear the SPI read and write buffers
	clear_SPI_buffers();

	// Put the commands for the MAX31723 device in the write buffer
	WriteBuffer[0] = MAX31723_TEMP_LSB_REG_ADDRESS;//[0]
	WriteBuffer[1] = 0x00000000;//[1]

	// Transmit the data.
	SPI_TransferInProgress = TRUE;
	Status =  XSpi_Transfer(SpiInstance,WriteBuffer,ReadBuffer,2);
	if (Status != XST_SUCCESS) return XST_FAILURE;

	while (SPI_TransferInProgress);  // Wait here until the SPI transfer has finished

	// Fetch the byte of data from the ReadBuffer
	Temperature_LSB = ReadBuffer[1]; //


	if (Temperature_MSB & 0x80)  // If the sign bit is a '1'
	{
		Temperature_LSB_float = (float)Temperature_LSB;

		Temperature_MSB = (~Temperature_MSB) + 1;
		Temperature_MSB_float = 0 - (float)Temperature_MSB;
		Temperature_LSB_float = 0;
		for (i=0; i<4; i++)
		{
			if (Temperature_LSB & (0x80 >> i))
			{
				Temperature_LSB_float += 0.5 / pow(2, i);  // For this to work, the -lm switch
				                                           // must be added to the linker command line
			}
		}
	}
	else
	{
		Temperature_LSB_float = (float)Temperature_LSB / 256;
		Temperature_MSB_float = (float)Temperature_MSB;
	}
	Temperature_float = Temperature_MSB_float + Temperature_LSB_float + TEMPERATURE_CALIBRATION_OFFSET;

	return (Temperature_float);
}
