import obd

conn = obd.OBD()


cmd = {
    '1-20': obd.commands.PIDS_A,
    'vin': obd.commands.VIN,
    'dtc': obd.commands.GET_DTC,
    'oil_temp': obd.commands.OIL_TEMP,
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

}

for id,command in cmd.items():
    if obd.commands.has_command(command):
        resp = conn.query(command)
    # if 'is not supported' in resp:
    #     pass
        if not 'is not supported' in resp.messages:
            print(f'{id}: ', resp.value)
        # else:
            # print(f'{id}: ', 'Not Supported')
# cmd = obd.commands.RUN_TIME
# resp = conn.query(cmd)
# print(resp.value.to('minutes'))
# print('VIN' in obd.commands)