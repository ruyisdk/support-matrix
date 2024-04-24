# Base of this file comes from: https://github.com/Community-PIO-CH32V/platform-ch32v


TOOL_CHAIN_PATH ?= ../../../../MRS_Toolchain_Linux_x64_V1.91/RISC-V_Embedded_GCC/bin
CROSS=riscv-none-embed-
ARCH=rv32imac
# Comment out above and enable below for gcc 13.2:
#TOOL_CHAIN_PATH ?= /opt/gcc-riscv/riscv-none-elf-gcc-13.2.0-2/bin
#CROSS=riscv-none-elf-
#ARCH=rv32imac_zicsr

OPENOCD_PATH    ?= ../../../../MRS_Toolchain_Linux_x64_V1.91/OpenOCD/bin
PROJECT_NAME    = freertos

TOP_DIR     := $(shell pwd)
OUTPUT_DIR  := $(TOP_DIR)/Build
STARTUP_DIR := $(TOP_DIR)/Startup
CORE_DIR    := $(TOP_DIR)/Core
DEBUG_DIR   := $(TOP_DIR)/Debug
SPL_DIR     := $(TOP_DIR)/Peripheral
USER_DIR    := $(TOP_DIR)/User
RTOS_DIR    := $(TOP_DIR)/FreeRTOS

LD_FILE     := $(TOP_DIR)/Ld/Link.ld
OPENOCD_FILE := ./wch-riscv.cfg
MAP_FILE    := $(OUTPUT_DIR)/$(PROJECT_NAME).map
ELF_FILE    := $(OUTPUT_DIR)/$(PROJECT_NAME).elf
HEX_FILE    := $(OUTPUT_DIR)/$(PROJECT_NAME).hex
LST_FILE    := $(OUTPUT_DIR)/$(PROJECT_NAME).lst
SIZ_FILE    := $(OUTPUT_DIR)/$(PROJECT_NAME).siz

INCLUDES := $(INCLUDES)
INCLUDES += -I $(TOP_DIR)/User
INCLUDES += -I $(TOP_DIR)/Core
INCLUDES += -I $(TOP_DIR)/Debug
INCLUDES += -I $(TOP_DIR)/Peripheral/inc
INCLUDES += -I $(RTOS_DIR)/include -I $(RTOS_DIR)/portable/GCC/RISC-V/chip_specific_extensions/RV32I_PFIC_no_extensions -I $(RTOS_DIR)/portable/GCC/RISC-V

CCFLAGS := -march=$(ARCH) \
           -mabi=ilp32 \
           -msmall-data-limit=8 \
           -mno-save-restore \
           -Os \
           -fmessage-length=0 \
           -fsigned-char \
           -ffunction-sections \
           -fdata-sections \
           -Wunused -Wuninitialized -g

all: $(HEX_FILE) $(LST_FILE) $(SIZ_FILE)

STARTUP_SRCS := $(wildcard $(STARTUP_DIR)/*.S)
STARTUP_OBJS := $(patsubst $(STARTUP_DIR)/%.S, $(OUTPUT_DIR)/startup/%.o, $(STARTUP_SRCS)) # patsubst: in #3 replace #1 to #2

CORE_SRCS := $(wildcard $(CORE_DIR)/*.c)
CORE_OBJS := $(patsubst $(CORE_DIR)/%.c, $(OUTPUT_DIR)/core/%.o, $(CORE_SRCS))

DEBUG_SRCS := $(wildcard $(DEBUG_DIR)/*.c)
DEBUG_OBJS := $(patsubst $(DEBUG_DIR)/%.c, $(OUTPUT_DIR)/debug/%.o, $(DEBUG_SRCS))

SPL_SRCS := $(wildcard $(SPL_DIR)/src/*.c)
SPL_OBJS := $(patsubst $(SPL_DIR)/src/%.c, $(OUTPUT_DIR)/spl/%.o, $(SPL_SRCS))

USER_SRCS := $(wildcard $(USER_DIR)/*.c)
USER_OBJS := $(patsubst $(USER_DIR)/%.c, $(OUTPUT_DIR)/user/%.o, $(USER_SRCS))

# RTOS_SRCS := $(wildcard $(RTOS_DIR)/*.c)
# RTOS_SRCS += $(wildcard $(RTOS_DIR)/portable/GCC/RISC-V/*.c)
RTOS_SRCS := $(shell find $(RTOS_DIR) -name '*.c')
RTOS_OBJS := $(patsubst $(RTOS_DIR)/%.c, $(OUTPUT_DIR)/rtos/%.o, $(RTOS_SRCS))

# RTOS_ASRCS := $(wildcard $(RTOS_DIR)/*.S)
RTOS_ASRCS := $(shell find $(RTOS_DIR) -name '*.S')
RTOS_OBJS += $(patsubst $(RTOS_DIR)/%.S, $(OUTPUT_DIR)/rtos/%.o, $(RTOS_ASRCS))

$(OUTPUT_DIR)/startup/%.o: $(STARTUP_DIR)/%.S
	@mkdir -p $(@D)
	$(TOOL_CHAIN_PATH)/$(CROSS)gcc $(CCFLAGS) -x assembler -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

$(OUTPUT_DIR)/core/%.o: $(CORE_DIR)/%.c
	@mkdir -p $(@D)
	$(TOOL_CHAIN_PATH)/$(CROSS)gcc $(CCFLAGS) $(INCLUDES) -std=gnu99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

$(OUTPUT_DIR)/debug/%.o: $(DEBUG_DIR)/%.c
	@mkdir -p $(@D)
	$(TOOL_CHAIN_PATH)/$(CROSS)gcc $(CCFLAGS) $(INCLUDES) -std=gnu99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

$(OUTPUT_DIR)/spl/%.o: $(SPL_DIR)/src/%.c
	@mkdir -p $(@D)
	$(TOOL_CHAIN_PATH)/$(CROSS)gcc $(CCFLAGS) $(INCLUDES) -std=gnu99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

$(OUTPUT_DIR)/user/%.o: $(USER_DIR)/%.c
	@mkdir -p $(@D)
	$(TOOL_CHAIN_PATH)/$(CROSS)gcc $(CCFLAGS) $(INCLUDES) -std=gnu99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

$(OUTPUT_DIR)/rtos/%.o: $(RTOS_DIR)/%.c
	@mkdir -p $(@D)
	$(TOOL_CHAIN_PATH)/$(CROSS)gcc $(CCFLAGS) $(INCLUDES) -std=gnu99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

$(OUTPUT_DIR)/rtos/%.o: $(RTOS_DIR)/%.S
	@mkdir -p $(@D)
	$(TOOL_CHAIN_PATH)/$(CROSS)gcc $(CCFLAGS) $(INCLUDES) -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"

$(ELF_FILE): $(STARTUP_OBJS) $(CORE_OBJS) $(DEBUG_OBJS) $(SPL_OBJS) $(USER_OBJS) $(RTOS_OBJS)
	$(TOOL_CHAIN_PATH)/$(CROSS)gcc $(CCFLAGS) -T $(LD_FILE) -nostartfiles -Xlinker --gc-sections -Wl,-Map,$(MAP_FILE) --specs=nano.specs --specs=nosys.specs -o $(ELF_FILE) $(USER_OBJS) $(STARTUP_OBJS) $(CORE_OBJS) $(DEBUG_OBJS) $(SPL_OBJS) $(RTOS_OBJS)

$(HEX_FILE): $(ELF_FILE)
	$(TOOL_CHAIN_PATH)/$(CROSS)objcopy -O ihex $(ELF_FILE) $(HEX_FILE)

$(LST_FILE): $(ELF_FILE)
	$(TOOL_CHAIN_PATH)/$(CROSS)objdump --all-headers --demangle --disassemble $(ELF_FILE) > $(LST_FILE)

$(SIZ_FILE): $(ELF_FILE)
	$(TOOL_CHAIN_PATH)/$(CROSS)size --format=berkeley $(ELF_FILE)

.PHONY: prepare
prepare:
	@cd .. && cp -r FreeRTOS FreeRTOS.bak
	@cp -r ../../SRC/* .
	@cp -r ../FreeRTOS.bak/Ld/* ./Ld/

.PHONY: clean
clean:
	rm -f $(OUTPUT_DIR)/startup/*
	rm -f $(OUTPUT_DIR)/core/*
	rm -f $(OUTPUT_DIR)/debug/*
	rm -f $(OUTPUT_DIR)/spl/*
	rm -f $(OUTPUT_DIR)/user/*
	rm -rf $(OUTPUT_DIR)/rtos/*
	rm -f $(OUTPUT_DIR)/*.*

flash:
	@cd $(OPENOCD_PATH) && sudo ./openocd -f wch-riscv.cfg -c init -c halt -c "flash erase_sector wch_riscv 0 last " -c exit
	@cd $(OPENOCD_PATH) && sudo ./openocd -f $(OPENOCD_FILE) -c init -c halt -c "program $(ELF_FILE)" -c exit
	@cd $(OPENOCD_PATH) && sudo ./openocd -f $(OPENOCD_FILE) -c init -c halt -c "verify_image $(ELF_FILE)"    -c exit
	@cd $(OPENOCD_PATH) && sudo ./openocd -f wch-riscv.cfg -c init -c halt -c wlink_reset_resume    -c exit

reset:
	@cd $(OPENOCD_PATH) && sudo ./openocd -f $(OPENOCD_FILE) -c init -c halt -c wlink_reset_resume -c exit
