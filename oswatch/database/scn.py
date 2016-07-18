def recover_scn():
	scn_sql='''
	select dbms_flashback.get_system_change_number from dual
	'''