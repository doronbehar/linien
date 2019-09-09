csr_constants = {
    'fast_a_iir_a_shift': 23,
    'fast_a_iir_a_width': 25,
    'fast_a_iir_a_interval': 1,
    'fast_a_iir_a_latency': 2,
    'fast_a_iir_a_order': 1,
    'fast_a_iir_a_iterative': 0,
    'fast_a_iir_b_shift': 23,
    'fast_a_iir_b_width': 25,
    'fast_a_iir_b_interval': 5,
    'fast_a_iir_b_latency': 6,
    'fast_a_iir_b_order': 2,
    'fast_a_iir_b_iterative': 1,
    'fast_a_iir_c_shift': 23,
    'fast_a_iir_c_width': 25,
    'fast_a_iir_c_interval': 1,
    'fast_a_iir_c_latency': 2,
    'fast_a_iir_c_order': 1,
    'fast_a_iir_c_iterative': 0,
    'fast_a_iir_d_shift': 23,
    'fast_a_iir_d_width': 25,
    'fast_a_iir_d_interval': 1,
    'fast_a_iir_d_latency': 3,
    'fast_a_iir_d_order': 2,
    'fast_a_iir_d_iterative': 0,
    'fast_a_iir_e_shift': 23,
    'fast_a_iir_e_width': 25,
    'fast_a_iir_e_interval': 5,
    'fast_a_iir_e_latency': 6,
    'fast_a_iir_e_order': 2,
    'fast_a_iir_e_iterative': 1,
    'fast_b_iir_a_shift': 23,
    'fast_b_iir_a_width': 25,
    'fast_b_iir_a_interval': 1,
    'fast_b_iir_a_latency': 2,
    'fast_b_iir_a_order': 1,
    'fast_b_iir_a_iterative': 0,
    'fast_b_iir_b_shift': 23,
    'fast_b_iir_b_width': 25,
    'fast_b_iir_b_interval': 5,
    'fast_b_iir_b_latency': 6,
    'fast_b_iir_b_order': 2,
    'fast_b_iir_b_iterative': 1,
    'fast_b_iir_c_shift': 23,
    'fast_b_iir_c_width': 25,
    'fast_b_iir_c_interval': 1,
    'fast_b_iir_c_latency': 2,
    'fast_b_iir_c_order': 1,
    'fast_b_iir_c_iterative': 0,
    'fast_b_iir_d_shift': 23,
    'fast_b_iir_d_width': 25,
    'fast_b_iir_d_interval': 1,
    'fast_b_iir_d_latency': 3,
    'fast_b_iir_d_order': 2,
    'fast_b_iir_d_iterative': 0,
    'fast_b_iir_e_shift': 23,
    'fast_b_iir_e_width': 25,
    'fast_b_iir_e_interval': 5,
    'fast_b_iir_e_latency': 6,
    'fast_b_iir_e_order': 2,
    'fast_b_iir_e_iterative': 1,
    'root_sweep_shift': 24,
}

csr = {
    'dna_dna': (28, 0x000, 64, False),
    'fast_a_x_tap': (0, 0x000, 2, True),
    'fast_a_brk': (0, 0x001, 1, True),
    'fast_a_y_tap': (0, 0x002, 2, True),
    'fast_a_iir_a_z0': (0, 0x003, 27, True),
    'fast_a_iir_a_a1': (0, 0x007, 25, True),
    'fast_a_iir_a_b0': (0, 0x00b, 25, True),
    'fast_a_iir_a_b1': (0, 0x00f, 25, True),
    'fast_a_demod_delay': (0, 0x013, 32, True),
    'fast_a_demod_multiplier': (0, 0x017, 4, True),
    'fast_a_iir_b_z0': (0, 0x018, 52, True),
    'fast_a_iir_b_a1': (0, 0x01f, 25, True),
    'fast_a_iir_b_a2': (0, 0x023, 25, True),
    'fast_a_iir_b_b0': (0, 0x027, 25, True),
    'fast_a_iir_b_b1': (0, 0x02b, 25, True),
    'fast_a_iir_b_b2': (0, 0x02f, 25, True),
    'fast_a_x_limit_min': (0, 0x033, 25, True),
    'fast_a_x_limit_max': (0, 0x037, 25, True),
    'fast_a_iir_c_z0': (0, 0x03b, 27, True),
    'fast_a_iir_c_a1': (0, 0x03f, 25, True),
    'fast_a_iir_c_b0': (0, 0x043, 25, True),
    'fast_a_iir_c_b1': (0, 0x047, 25, True),
    'fast_a_iir_d_z0': (0, 0x04b, 27, True),
    'fast_a_iir_d_a1': (0, 0x04f, 25, True),
    'fast_a_iir_d_a2': (0, 0x053, 25, True),
    'fast_a_iir_d_b0': (0, 0x057, 25, True),
    'fast_a_iir_d_b1': (0, 0x05b, 25, True),
    'fast_a_iir_d_b2': (0, 0x05f, 25, True),
    'fast_a_iir_e_z0': (0, 0x063, 52, True),
    'fast_a_iir_e_a1': (0, 0x06a, 25, True),
    'fast_a_iir_e_a2': (0, 0x06e, 25, True),
    'fast_a_iir_e_b0': (0, 0x072, 25, True),
    'fast_a_iir_e_b1': (0, 0x076, 25, True),
    'fast_a_iir_e_b2': (0, 0x07a, 25, True),
    'fast_a_y_limit_min': (0, 0x07e, 14, True),
    'fast_a_y_limit_max': (0, 0x080, 14, True),
    'fast_a_x_clr': (0, 0x082, 1, True),
    'fast_a_x_max': (0, 0x083, 25, False),
    'fast_a_x_min': (0, 0x087, 25, False),
    'fast_a_y_clr': (0, 0x08b, 1, True),
    'fast_a_y_max': (0, 0x08c, 25, False),
    'fast_a_y_min': (0, 0x090, 25, False),
    'fast_a_x_hold_en': (0, 0x094, 17, True),
    'fast_a_x_clear_en': (0, 0x097, 17, True),
    'fast_a_y_hold_en': (0, 0x09a, 17, True),
    'fast_a_y_clear_en': (0, 0x09d, 17, True),
    'fast_a_dx_sel': (0, 0x0a0, 4, True),
    'fast_a_dy_sel': (0, 0x0a1, 4, True),
    'fast_a_rx_sel': (0, 0x0a2, 4, True),
    'fast_b_x_tap': (1, 0x000, 2, True),
    'fast_b_brk': (1, 0x001, 1, True),
    'fast_b_y_tap': (1, 0x002, 2, True),
    'fast_b_iir_a_z0': (1, 0x003, 27, True),
    'fast_b_iir_a_a1': (1, 0x007, 25, True),
    'fast_b_iir_a_b0': (1, 0x00b, 25, True),
    'fast_b_iir_a_b1': (1, 0x00f, 25, True),
    'fast_b_demod_delay': (1, 0x013, 32, True),
    'fast_b_demod_multiplier': (1, 0x017, 4, True),
    'fast_b_iir_b_z0': (1, 0x018, 52, True),
    'fast_b_iir_b_a1': (1, 0x01f, 25, True),
    'fast_b_iir_b_a2': (1, 0x023, 25, True),
    'fast_b_iir_b_b0': (1, 0x027, 25, True),
    'fast_b_iir_b_b1': (1, 0x02b, 25, True),
    'fast_b_iir_b_b2': (1, 0x02f, 25, True),
    'fast_b_x_limit_min': (1, 0x033, 25, True),
    'fast_b_x_limit_max': (1, 0x037, 25, True),
    'fast_b_iir_c_z0': (1, 0x03b, 27, True),
    'fast_b_iir_c_a1': (1, 0x03f, 25, True),
    'fast_b_iir_c_b0': (1, 0x043, 25, True),
    'fast_b_iir_c_b1': (1, 0x047, 25, True),
    'fast_b_iir_d_z0': (1, 0x04b, 27, True),
    'fast_b_iir_d_a1': (1, 0x04f, 25, True),
    'fast_b_iir_d_a2': (1, 0x053, 25, True),
    'fast_b_iir_d_b0': (1, 0x057, 25, True),
    'fast_b_iir_d_b1': (1, 0x05b, 25, True),
    'fast_b_iir_d_b2': (1, 0x05f, 25, True),
    'fast_b_iir_e_z0': (1, 0x063, 52, True),
    'fast_b_iir_e_a1': (1, 0x06a, 25, True),
    'fast_b_iir_e_a2': (1, 0x06e, 25, True),
    'fast_b_iir_e_b0': (1, 0x072, 25, True),
    'fast_b_iir_e_b1': (1, 0x076, 25, True),
    'fast_b_iir_e_b2': (1, 0x07a, 25, True),
    'fast_b_y_limit_min': (1, 0x07e, 14, True),
    'fast_b_y_limit_max': (1, 0x080, 14, True),
    'fast_b_x_clr': (1, 0x082, 1, True),
    'fast_b_x_max': (1, 0x083, 25, False),
    'fast_b_x_min': (1, 0x087, 25, False),
    'fast_b_y_clr': (1, 0x08b, 1, True),
    'fast_b_y_max': (1, 0x08c, 25, False),
    'fast_b_y_min': (1, 0x090, 25, False),
    'fast_b_x_hold_en': (1, 0x094, 17, True),
    'fast_b_x_clear_en': (1, 0x097, 17, True),
    'fast_b_y_hold_en': (1, 0x09a, 17, True),
    'fast_b_y_clear_en': (1, 0x09d, 17, True),
    'fast_b_dx_sel': (1, 0x0a0, 4, True),
    'fast_b_dy_sel': (1, 0x0a1, 4, True),
    'fast_b_rx_sel': (1, 0x0a2, 4, True),
    'gpio_n_ins': (30, 0x000, 8, False),
    'gpio_n_outs': (30, 0x001, 8, True),
    'gpio_n_oes': (30, 0x002, 8, True),
    'gpio_n_state': (30, 0x003, 17, False),
    'gpio_n_state_clr': (30, 0x006, 1, True),
    'gpio_n_do0_en': (30, 0x007, 17, True),
    'gpio_n_do1_en': (30, 0x00a, 17, True),
    'gpio_n_do2_en': (30, 0x00d, 17, True),
    'gpio_n_do3_en': (30, 0x010, 17, True),
    'gpio_n_do4_en': (30, 0x013, 17, True),
    'gpio_n_do5_en': (30, 0x016, 17, True),
    'gpio_n_do6_en': (30, 0x019, 17, True),
    'gpio_n_do7_en': (30, 0x01c, 17, True),
    'gpio_p_ins': (31, 0x000, 8, False),
    'gpio_p_outs': (31, 0x001, 8, True),
    'gpio_p_oes': (31, 0x002, 8, True),
    'root_chain_a_factor': (8, 0x000, 9, True),
    'root_chain_b_factor': (8, 0x002, 9, True),
    'root_chain_a_offset': (8, 0x004, 14, True),
    'root_chain_b_offset': (8, 0x006, 14, True),
    'root_combined_offset': (8, 0x008, 14, True),
    'root_out_offset': (8, 0x00a, 14, True),
    'root_mod_channel': (8, 0x00c, 1, True),
    'root_control_channel': (8, 0x00d, 1, True),
    'root_sweep_channel': (8, 0x00e, 2, True),
    'root_slow_value': (8, 0x00f, 14, False),
    'root_mod_amp': (8, 0x011, 14, True),
    'root_mod_freq': (8, 0x013, 32, True),
    'root_sweep_step': (8, 0x017, 30, True),
    'root_sweep_min': (8, 0x01b, 14, True),
    'root_sweep_max': (8, 0x01d, 14, True),
    'root_sweep_run': (8, 0x01f, 1, True),
    'root_limit_error_signal_min': (8, 0x020, 14, True),
    'root_limit_error_signal_max': (8, 0x022, 14, True),
    'root_limit_fast1_min': (8, 0x024, 14, True),
    'root_limit_fast1_max': (8, 0x026, 14, True),
    'root_limit_fast2_min': (8, 0x028, 14, True),
    'root_limit_fast2_max': (8, 0x02a, 14, True),
    'root_pid_setpoint': (8, 0x02c, 14, True),
    'root_pid_kp': (8, 0x02e, 14, True),
    'root_pid_ki': (8, 0x030, 14, True),
    'root_pid_reset': (8, 0x032, 1, True),
    'root_pid_kd': (8, 0x033, 14, True),
    'root_slow_decimation': (8, 0x035, 5, True),
    'root_watcher_reset': (8, 0x036, 1, True),
    'root_watcher_lock_lost': (8, 0x037, 1, False),
    'root_watcher_time_constant': (8, 0x038, 20, True),
    'root_watcher_threshold': (8, 0x03b, 14, True),
    'root_control_signal_clr': (8, 0x03d, 1, True),
    'root_control_signal_max': (8, 0x03e, 25, False),
    'root_control_signal_min': (8, 0x042, 25, False),
    'root_combined_error_signal_clr': (8, 0x046, 1, True),
    'root_combined_error_signal_max': (8, 0x047, 25, False),
    'root_combined_error_signal_min': (8, 0x04b, 25, False),
    'scopegen_external_trigger': (6, 0x000, 1, True),
    'scopegen_dac_a_clr': (6, 0x001, 1, True),
    'scopegen_dac_a_max': (6, 0x002, 25, False),
    'scopegen_dac_a_min': (6, 0x006, 25, False),
    'scopegen_dac_b_clr': (6, 0x00a, 1, True),
    'scopegen_dac_b_max': (6, 0x00b, 25, False),
    'scopegen_dac_b_min': (6, 0x00f, 25, False),
    'scopegen_adc_a_sel': (6, 0x013, 4, True),
    'scopegen_adc_b_sel': (6, 0x014, 4, True),
    'slow_pid_setpoint': (2, 0x000, 14, True),
    'slow_pid_kp': (2, 0x002, 14, True),
    'slow_pid_ki': (2, 0x004, 14, True),
    'slow_pid_reset': (2, 0x006, 1, True),
    'slow_pid_kd': (2, 0x007, 14, True),
    'slow_limit_min': (2, 0x009, 14, True),
    'slow_limit_max': (2, 0x00b, 14, True),
    'slow_out_clr': (2, 0x00d, 1, True),
    'slow_out_max': (2, 0x00e, 25, False),
    'slow_out_min': (2, 0x012, 25, False),
    'xadc_temp': (29, 0x000, 12, False),
    'xadc_v': (29, 0x002, 12, False),
    'xadc_a': (29, 0x004, 12, False),
    'xadc_b': (29, 0x006, 12, False),
    'xadc_c': (29, 0x008, 12, False),
    'xadc_d': (29, 0x00a, 12, False),
}
states = ['force', 'di0', 'di1', 'di2', 'di3', 'di4', 'di5', 'di6', 'di7', 'fast_a_x_sat', 'fast_a_x_railed', 'fast_a_y_sat', 'fast_a_y_railed', 'fast_b_x_sat', 'fast_b_x_railed', 'fast_b_y_sat', 'fast_b_y_railed']
signals = ['zero', 'fast_a_x', 'fast_a_y', 'fast_b_x', 'fast_b_y', 'slow_out', 'scopegen_dac_a', 'scopegen_dac_b', 'root_control_signal', 'root_combined_error_signal']
