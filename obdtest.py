import obd

conn = obd.OBD()


cmd = {
    # 'base_commands': obd.commands.base_commands(),
    '1-20': obd.commands.PIDS_A,
    'vin': obd.commands.VIN,
    'dtc': obd.commands.GET_DTC,
    'oil_temp': obd.commands.OIL_TEMP,
    'coolant_temp': obd.commands.COOLANT_TEMP,
    'ambiant_air_temp': obd.commands.AMBIANT_AIR_TEMP,
    'intake_press': obd.commands.INTAKE_PRESSURE,
    'fuel_pressure': obd.commands.FUEL_PRESSURE,
    'intake_temp': obd.commands.INTAKE_TEMP,
    'short_trim': obd.commands.SHORT_FUEL_TRIM_1,
    'long_trim': obd.commands.LONG_FUEL_TRIM_1,
    'maf': obd.commands.MAF,
    'rpm': obd.commands.RPM,
    'timing_adv': obd.commands.TIMING_ADVANCE,
    'throttle_pos': obd.commands.THROTTLE_POS,
    'o2s': obd.commands.O2_SENSORS,
    'o2_b1s1': obd.commands.O2_B1S1,
    'o2_b1s2': obd.commands.O2_B1S2,
    'o2_b1s3': obd.commands.O2_B1S3,
    'o2_b1s4': obd.commands.O2_B1S4,
    'o2_b2s1': obd.commands.O2_B2S1,
    'o2_b2s2': obd.commands.O2_B2S2,
    'o2_b3s3': obd.commands.O2_B2S3,
    'o2_b4s4': obd.commands.O2_B2S4,
    'run_time': obd.commands.RUN_TIME,
    'engine_load': obd.commands.ENGINE_LOAD,
    'freeze_dtc': obd.commands.FREEZE_DTC,
    'distance_w_mil': obd.commands.DISTANCE_W_MIL,
    'fuel_level': obd.commands.FUEL_LEVEL,
    'commanded_egr': obd.commands.COMMANDED_EGR,
    'fuel_rail_pressure_vac': obd.commands.FUEL_RAIL_PRESSURE_VAC,
    'frp_direct': obd.commands.FUEL_RAIL_PRESSURE_DIRECT,
    'o2s1_wr_voltage': obd.commands.O2_S1_WR_VOLTAGE,
    'o2s2_wr_voltage': obd.commands.O2_S2_WR_VOLTAGE,
    'o2s3_wr_voltage': obd.commands.O2_S3_WR_VOLTAGE,
    'o2s4_wr_voltage': obd.commands.O2_S4_WR_VOLTAGE,
    'o2s5_wr_voltage': obd.commands.O2_S5_WR_VOLTAGE,
    'o2s6_wr_voltage': obd.commands.O2_S6_WR_VOLTAGE,
    'o2s7_wr_voltage': obd.commands.O2_S7_WR_VOLTAGE,
    'o2s8_wr_voltage': obd.commands.O2_S8_WR_VOLTAGE,
    'egr_error': obd.commands.EGR_ERROR,
    'evap_purge': obd.commands.EVAPORATIVE_PURGE,
    'warmups_since_dtc_clear': obd.commands.WARMUPS_SINCE_DTC_CLEAR,
    'distance_since_dtc_clear': obd.commands.DISTANCE_SINCE_DTC_CLEAR,
    'evac_vap_pressure': obd.commands.EVAP_VAPOR_PRESSURE,
    'baro_pressure': obd.commands.BAROMETRIC_PRESSURE,
    'o2s1_wr_current': obd.commands.O2_S1_WR_CURRENT,
    'o2s2_wr_current': obd.commands.O2_S2_WR_CURRENT,
    'o2s3_wr_current': obd.commands.O2_S3_WR_CURRENT,
    'o2s4_wr_current': obd.commands.O2_S4_WR_CURRENT,
    'o2s5_wr_current': obd.commands.O2_S5_WR_CURRENT,
    'o2s6_wr_current': obd.commands.O2_S6_WR_CURRENT,
    'o2s7_wr_current': obd.commands.O2_S7_WR_CURRENT,
    'o2s8_wr_current': obd.commands.O2_S8_WR_CURRENT,
    'cat_temp_b1s1': obd.commands.CATALYST_TEMP_B1S1,
    'cat_temp_b1s2': obd.commands.CATALYST_TEMP_B1S2,
    'cat_temp_b2s1': obd.commands.CATALYST_TEMP_B2S1,
    'cat_temp_b2s2': obd.commands.CATALYST_TEMP_B2S2,
    'status_drive_cycle': obd.commands.STATUS_DRIVE_CYCLE,
    'control_module_voltage': obd.commands.CONTROL_MODULE_VOLTAGE,
    'absolute_load': obd.commands.ABSOLUTE_LOAD,
    'commanded_equiv_ratio': obd.commands.COMMANDED_EQUIV_RATIO,
    'relative_throttle_pos': obd.commands.RELATIVE_THROTTLE_POS,
    'ambiant_air_temp': obd.commands.AMBIANT_AIR_TEMP,
    'throttle_pos_b': obd.commands.THROTTLE_POS_B,
    'fuel_rail_pressure_absolute': obd.commands.FUEL_RAIL_PRESSURE_ABS,
    'fuel_injection_timing': obd.commands.FUEL_INJECT_TIMING,
    'obd_voltage': obd.commands.ELM_VOLTAGE,
    'elm_version': obd.commands.ELM_VERSION,





}
# obd.commands.base_commands()
for id,command in cmd.items():
    # if conn.supports(command):
    if "1-20" in id:
        resp = conn.query(command)
        print(f'{id}, {resp.command.name}')
    resp = conn.query(command, force=True)
    # if resp.unit == 'degC':
    #     print(f'{resp.command.desc}: {resp.value.to("fahrenheit")}')
    # elif resp.unit == 'kph':
    #     print(f'{resp.command.desc}: {resp.value.to("mph")}')
    # elif resp.unit == 'kilometer':
    #     print(f'{resp.command.desc}: {resp.value.to("mile")}')
    # elif resp.unit == 'second':
    #     print(f'{resp.command.desc}: {resp.value.to("hour")}')
    # else:
    #     print(f'{resp.command.desc}: {resp.value}')

    if "Monitor status" in resp.command.desc:
        print(f'{resp.command.desc}: ', resp.value.FUEL_SYSTEM_MONITORING.available)

# import obd
# import time

# connection = obd.Async()

# # a callback that prints every new value to the console
# def new_rpm(r):
#     print(r.value)

# connection.watch(obd.commands.SHORT_FUEL_TRIM_1, callback=new_rpm)
# connection.start()

# # the callback will now be fired upon receipt of new values

# time.sleep(60)
# connection.stop()