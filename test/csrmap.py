csr = {
    'dna_dna': (0x4030e000, 64, False),
    'fast_a_x_tap': (0x40300000, 2, True),
    'fast_a_break': (0x40300004, 1, True),
    'fast_a_y_tap': (0x40300008, 2, True),
    'fast_a_iir_a_z0': (0x4030000c, 27, True),
    'fast_a_iir_a_shift': (0x4030001c, 5, False),
    'fast_a_iir_a_width': (0x40300020, 5, False),
    'fast_a_iir_a_interval': (0x40300024, 8, False),
    'fast_a_iir_a_a1': (0x40300028, 18, True),
    'fast_a_iir_a_b0': (0x40300034, 18, True),
    'fast_a_iir_a_b1': (0x40300040, 18, True),
    'fast_a_demod_phase': (0x4030004c, 14, True),
    'fast_a_iir_b_z0': (0x40300054, 38, True),
    'fast_a_iir_b_shift': (0x40300068, 5, False),
    'fast_a_iir_b_width': (0x4030006c, 5, False),
    'fast_a_iir_b_interval': (0x40300070, 8, False),
    'fast_a_iir_b_a1': (0x40300074, 25, True),
    'fast_a_iir_b_a2': (0x40300084, 25, True),
    'fast_a_iir_b_b0': (0x40300094, 25, True),
    'fast_a_iir_b_b1': (0x403000a4, 25, True),
    'fast_a_iir_b_b2': (0x403000b4, 25, True),
    'fast_a_x_limit_min': (0x403000c4, 25, True),
    'fast_a_x_limit_max': (0x403000d4, 25, True),
    'fast_a_iir_c_z0': (0x403000e4, 27, True),
    'fast_a_iir_c_shift': (0x403000f4, 5, False),
    'fast_a_iir_c_width': (0x403000f8, 5, False),
    'fast_a_iir_c_interval': (0x403000fc, 8, False),
    'fast_a_iir_c_a1': (0x40300100, 18, True),
    'fast_a_iir_c_b0': (0x4030010c, 18, True),
    'fast_a_iir_c_b1': (0x40300118, 18, True),
    'fast_a_iir_d_z0': (0x40300124, 27, True),
    'fast_a_iir_d_shift': (0x40300134, 5, False),
    'fast_a_iir_d_width': (0x40300138, 5, False),
    'fast_a_iir_d_interval': (0x4030013c, 8, False),
    'fast_a_iir_d_a1': (0x40300140, 18, True),
    'fast_a_iir_d_a2': (0x4030014c, 18, True),
    'fast_a_iir_d_b0': (0x40300158, 18, True),
    'fast_a_iir_d_b1': (0x40300164, 18, True),
    'fast_a_iir_d_b2': (0x40300170, 18, True),
    'fast_a_iir_e_z0': (0x4030017c, 38, True),
    'fast_a_iir_e_shift': (0x40300190, 5, False),
    'fast_a_iir_e_width': (0x40300194, 5, False),
    'fast_a_iir_e_interval': (0x40300198, 8, False),
    'fast_a_iir_e_a1': (0x4030019c, 25, True),
    'fast_a_iir_e_a2': (0x403001ac, 25, True),
    'fast_a_iir_e_b0': (0x403001bc, 25, True),
    'fast_a_iir_e_b1': (0x403001cc, 25, True),
    'fast_a_iir_e_b2': (0x403001dc, 25, True),
    'fast_a_relock_shift': (0x403001ec, 5, False),
    'fast_a_relock_step': (0x403001f0, 24, True),
    'fast_a_relock_run': (0x403001fc, 1, True),
    'fast_a_relock_min': (0x40300200, 15, True),
    'fast_a_relock_max': (0x40300208, 15, True),
    'fast_a_sweep_shift': (0x40300210, 5, False),
    'fast_a_sweep_step': (0x40300214, 24, True),
    'fast_a_sweep_min': (0x40300220, 14, True),
    'fast_a_sweep_max': (0x40300228, 14, True),
    'fast_a_sweep_run': (0x40300230, 1, True),
    'fast_a_mod_freq': (0x40300234, 32, True),
    'fast_a_mod_amp': (0x40300244, 14, True),
    'fast_a_y_limit_min': (0x4030024c, 14, True),
    'fast_a_y_limit_max': (0x40300254, 14, True),
    'fast_a_x_hold_en': (0x4030025c, 27, True),
    'fast_a_x_clear_en': (0x4030026c, 27, True),
    'fast_a_y_hold_en': (0x4030027c, 27, True),
    'fast_a_y_clear_en': (0x4030028c, 27, True),
    'fast_a_relock_en': (0x4030029c, 27, True),
    'fast_a_dx_sel': (0x403002ac, 5, True),
    'fast_a_dy_sel': (0x403002b0, 5, True),
    'fast_a_rx_sel': (0x403002b4, 5, True),
    'fast_b_x_tap': (0x40300800, 2, True),
    'fast_b_break': (0x40300804, 1, True),
    'fast_b_y_tap': (0x40300808, 2, True),
    'fast_b_iir_a_z0': (0x4030080c, 27, True),
    'fast_b_iir_a_shift': (0x4030081c, 5, False),
    'fast_b_iir_a_width': (0x40300820, 5, False),
    'fast_b_iir_a_interval': (0x40300824, 8, False),
    'fast_b_iir_a_a1': (0x40300828, 18, True),
    'fast_b_iir_a_b0': (0x40300834, 18, True),
    'fast_b_iir_a_b1': (0x40300840, 18, True),
    'fast_b_demod_phase': (0x4030084c, 14, True),
    'fast_b_iir_b_z0': (0x40300854, 38, True),
    'fast_b_iir_b_shift': (0x40300868, 5, False),
    'fast_b_iir_b_width': (0x4030086c, 5, False),
    'fast_b_iir_b_interval': (0x40300870, 8, False),
    'fast_b_iir_b_a1': (0x40300874, 25, True),
    'fast_b_iir_b_a2': (0x40300884, 25, True),
    'fast_b_iir_b_b0': (0x40300894, 25, True),
    'fast_b_iir_b_b1': (0x403008a4, 25, True),
    'fast_b_iir_b_b2': (0x403008b4, 25, True),
    'fast_b_x_limit_min': (0x403008c4, 25, True),
    'fast_b_x_limit_max': (0x403008d4, 25, True),
    'fast_b_iir_c_z0': (0x403008e4, 27, True),
    'fast_b_iir_c_shift': (0x403008f4, 5, False),
    'fast_b_iir_c_width': (0x403008f8, 5, False),
    'fast_b_iir_c_interval': (0x403008fc, 8, False),
    'fast_b_iir_c_a1': (0x40300900, 18, True),
    'fast_b_iir_c_b0': (0x4030090c, 18, True),
    'fast_b_iir_c_b1': (0x40300918, 18, True),
    'fast_b_iir_d_z0': (0x40300924, 27, True),
    'fast_b_iir_d_shift': (0x40300934, 5, False),
    'fast_b_iir_d_width': (0x40300938, 5, False),
    'fast_b_iir_d_interval': (0x4030093c, 8, False),
    'fast_b_iir_d_a1': (0x40300940, 18, True),
    'fast_b_iir_d_a2': (0x4030094c, 18, True),
    'fast_b_iir_d_b0': (0x40300958, 18, True),
    'fast_b_iir_d_b1': (0x40300964, 18, True),
    'fast_b_iir_d_b2': (0x40300970, 18, True),
    'fast_b_iir_e_z0': (0x4030097c, 38, True),
    'fast_b_iir_e_shift': (0x40300990, 5, False),
    'fast_b_iir_e_width': (0x40300994, 5, False),
    'fast_b_iir_e_interval': (0x40300998, 8, False),
    'fast_b_iir_e_a1': (0x4030099c, 25, True),
    'fast_b_iir_e_a2': (0x403009ac, 25, True),
    'fast_b_iir_e_b0': (0x403009bc, 25, True),
    'fast_b_iir_e_b1': (0x403009cc, 25, True),
    'fast_b_iir_e_b2': (0x403009dc, 25, True),
    'fast_b_relock_shift': (0x403009ec, 5, False),
    'fast_b_relock_step': (0x403009f0, 24, True),
    'fast_b_relock_run': (0x403009fc, 1, True),
    'fast_b_relock_min': (0x40300a00, 15, True),
    'fast_b_relock_max': (0x40300a08, 15, True),
    'fast_b_sweep_shift': (0x40300a10, 5, False),
    'fast_b_sweep_step': (0x40300a14, 24, True),
    'fast_b_sweep_min': (0x40300a20, 14, True),
    'fast_b_sweep_max': (0x40300a28, 14, True),
    'fast_b_sweep_run': (0x40300a30, 1, True),
    'fast_b_mod_freq': (0x40300a34, 32, True),
    'fast_b_mod_amp': (0x40300a44, 14, True),
    'fast_b_y_limit_min': (0x40300a4c, 14, True),
    'fast_b_y_limit_max': (0x40300a54, 14, True),
    'fast_b_x_hold_en': (0x40300a5c, 27, True),
    'fast_b_x_clear_en': (0x40300a6c, 27, True),
    'fast_b_y_hold_en': (0x40300a7c, 27, True),
    'fast_b_y_clear_en': (0x40300a8c, 27, True),
    'fast_b_relock_en': (0x40300a9c, 27, True),
    'fast_b_dx_sel': (0x40300aac, 5, True),
    'fast_b_dy_sel': (0x40300ab0, 5, True),
    'fast_b_rx_sel': (0x40300ab4, 5, True),
    'gpio_n_in': (0x4030f000, 8, False),
    'gpio_n_out': (0x4030f004, 8, True),
    'gpio_n_oe': (0x4030f008, 8, True),
    'gpio_n_do0_en': (0x4030f00c, 27, True),
    'gpio_n_do1_en': (0x4030f01c, 27, True),
    'gpio_n_do2_en': (0x4030f02c, 27, True),
    'gpio_n_do3_en': (0x4030f03c, 27, True),
    'gpio_n_do4_en': (0x4030f04c, 27, True),
    'gpio_n_do5_en': (0x4030f05c, 27, True),
    'gpio_n_do6_en': (0x4030f06c, 27, True),
    'gpio_n_do7_en': (0x4030f07c, 27, True),
    'gpio_p_in': (0x4030f800, 8, False),
    'gpio_p_out': (0x4030f804, 8, True),
    'gpio_p_oe': (0x4030f808, 8, True),
    'noise_bits': (0x40303800, 5, True),
    'scopegen_adc_a_sel': (0x40303000, 5, True),
    'scopegen_adc_b_sel': (0x40303004, 5, True),
    'slow_a_break': (0x40301000, 1, True),
    'slow_a_x_limit_min': (0x40301004, 25, True),
    'slow_a_x_limit_max': (0x40301014, 25, True),
    'slow_a_iir_z0': (0x40301024, 38, True),
    'slow_a_iir_shift': (0x40301038, 5, False),
    'slow_a_iir_width': (0x4030103c, 5, False),
    'slow_a_iir_interval': (0x40301040, 8, False),
    'slow_a_iir_a1': (0x40301044, 25, True),
    'slow_a_iir_a2': (0x40301054, 25, True),
    'slow_a_iir_b0': (0x40301064, 25, True),
    'slow_a_iir_b1': (0x40301074, 25, True),
    'slow_a_iir_b2': (0x40301084, 25, True),
    'slow_a_y_limit_min': (0x40301094, 16, True),
    'slow_a_y_limit_max': (0x4030109c, 16, True),
    'slow_a_hold_en': (0x403010a4, 27, True),
    'slow_a_clear_en': (0x403010b4, 27, True),
    'slow_a_dx_sel': (0x403010c4, 5, True),
    'slow_b_break': (0x40301800, 1, True),
    'slow_b_x_limit_min': (0x40301804, 25, True),
    'slow_b_x_limit_max': (0x40301814, 25, True),
    'slow_b_iir_z0': (0x40301824, 38, True),
    'slow_b_iir_shift': (0x40301838, 5, False),
    'slow_b_iir_width': (0x4030183c, 5, False),
    'slow_b_iir_interval': (0x40301840, 8, False),
    'slow_b_iir_a1': (0x40301844, 25, True),
    'slow_b_iir_a2': (0x40301854, 25, True),
    'slow_b_iir_b0': (0x40301864, 25, True),
    'slow_b_iir_b1': (0x40301874, 25, True),
    'slow_b_iir_b2': (0x40301884, 25, True),
    'slow_b_y_limit_min': (0x40301894, 16, True),
    'slow_b_y_limit_max': (0x4030189c, 16, True),
    'slow_b_hold_en': (0x403018a4, 27, True),
    'slow_b_clear_en': (0x403018b4, 27, True),
    'slow_b_dx_sel': (0x403018c4, 5, True),
    'slow_c_break': (0x40302000, 1, True),
    'slow_c_x_limit_min': (0x40302004, 25, True),
    'slow_c_x_limit_max': (0x40302014, 25, True),
    'slow_c_iir_z0': (0x40302024, 38, True),
    'slow_c_iir_shift': (0x40302038, 5, False),
    'slow_c_iir_width': (0x4030203c, 5, False),
    'slow_c_iir_interval': (0x40302040, 8, False),
    'slow_c_iir_a1': (0x40302044, 25, True),
    'slow_c_iir_a2': (0x40302054, 25, True),
    'slow_c_iir_b0': (0x40302064, 25, True),
    'slow_c_iir_b1': (0x40302074, 25, True),
    'slow_c_iir_b2': (0x40302084, 25, True),
    'slow_c_y_limit_min': (0x40302094, 16, True),
    'slow_c_y_limit_max': (0x4030209c, 16, True),
    'slow_c_hold_en': (0x403020a4, 27, True),
    'slow_c_clear_en': (0x403020b4, 27, True),
    'slow_c_dx_sel': (0x403020c4, 5, True),
    'slow_d_break': (0x40302800, 1, True),
    'slow_d_x_limit_min': (0x40302804, 25, True),
    'slow_d_x_limit_max': (0x40302814, 25, True),
    'slow_d_iir_z0': (0x40302824, 38, True),
    'slow_d_iir_shift': (0x40302838, 5, False),
    'slow_d_iir_width': (0x4030283c, 5, False),
    'slow_d_iir_interval': (0x40302840, 8, False),
    'slow_d_iir_a1': (0x40302844, 25, True),
    'slow_d_iir_a2': (0x40302854, 25, True),
    'slow_d_iir_b0': (0x40302864, 25, True),
    'slow_d_iir_b1': (0x40302874, 25, True),
    'slow_d_iir_b2': (0x40302884, 25, True),
    'slow_d_y_limit_min': (0x40302894, 16, True),
    'slow_d_y_limit_max': (0x4030289c, 16, True),
    'slow_d_hold_en': (0x403028a4, 27, True),
    'slow_d_clear_en': (0x403028b4, 27, True),
    'slow_d_dx_sel': (0x403028c4, 5, True),
    'xadc_temp': (0x4030e800, 12, False),
    'xadc_pint': (0x4030e808, 12, False),
    'xadc_paux': (0x4030e810, 12, False),
    'xadc_bram': (0x4030e818, 12, False),
    'xadc_int': (0x4030e820, 12, False),
    'xadc_aux': (0x4030e828, 12, False),
    'xadc_ddr': (0x4030e830, 12, False),
    'xadc_v': (0x4030e838, 12, False),
    'xadc_a': (0x4030e840, 12, False),
    'xadc_b': (0x4030e848, 12, False),
    'xadc_c': (0x4030e850, 12, False),
    'xadc_d': (0x4030e858, 12, False),
}
states = ['force', 'di0', 'di1', 'di2', 'di3', 'di4', 'di5', 'di6', 'di7', 'fast_a_x_sat', 'fast_a_x_railed', 'fast_a_y_sat', 'fast_a_y_railed', 'fast_a_unlocked', 'fast_b_x_sat', 'fast_b_x_railed', 'fast_b_y_sat', 'fast_b_y_railed', 'fast_b_unlocked', 'slow_a_sat', 'slow_a_railed', 'slow_b_sat', 'slow_b_railed', 'slow_c_sat', 'slow_c_railed', 'slow_d_sat', 'slow_d_railed']
signals = ['zero', 'fast_a_x', 'fast_a_y', 'fast_b_x', 'fast_b_y', 'slow_a_x', 'slow_a_y', 'slow_b_x', 'slow_b_y', 'slow_c_x', 'slow_c_y', 'slow_d_x', 'slow_d_y', 'scopegen_dac_a', 'scopegen_dac_b', 'noise_y']
