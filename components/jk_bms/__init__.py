import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import jk_modbus
from esphome.const import CONF_ID

AUTO_LOAD = ["jk_modbus", "sensor", "switch", "text_sensor"]
CODEOWNERS = ["@syssi"]
MULTI_CONF = True

CONF_JK_BMS_ID = "jk_bms_id"

jk_bms_ns = cg.esphome_ns.namespace("jk_bms")
JkBms = jk_bms_ns.class_("JkBms", cg.PollingComponent, jk_modbus.JkModbusDevice)

CONFIG_SCHEMA = (
    cv.Schema({cv.GenerateID(): cv.declare_id(JkBms)})
    .extend(cv.polling_component_schema("5s"))
    .extend(jk_modbus.jk_modbus_device_schema(0x4E))
)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield jk_modbus.register_jk_modbus_device(var, config)