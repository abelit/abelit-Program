#!/bin/sh
ORACLE_BASE=/u01/app/oracle
ORACLE_HOME=/u01/app/oracle/product/11.2.0/db_1
ORACLE_SID=gzgszxk1
NLS_LANG=AMERICAN_AMERICA.ZHS16GBK
export ORACLE_BASE
export ORACLE_HOME
export ORACLE_SID
export NLS_LANG

exp \'/ as sysdba\' file=/u01/backup/GZGSNJ_GY.dmp owner=GZGSNJ_GY
exp \'/ as sysdba\' file=/u01/backup/GZGS_LPS.dmp owner=GZGS_LPS
exp \'/ as sysdba\' file=/u01/backup/GZGS_ZY.dmp owner=GZGS_ZY
exp \'/ as sysdba\' file=/u01/backup/GZGSNJ_AS.dmp owner=GZGSNJ_AS
exp \'/ as sysdba\' file=/u01/backup/GZGS_QXN.dmp owner=GZGS_QXN
exp \'/ as sysdba\' file=/u01/backup/GZGS_AJCX.dmp owner=GZGS_AJCX
exp \'/ as sysdba\' file=/u01/backup/GZGS_CREDIT.dmp owner=GZGS_CREDIT
exp \'/ as sysdba\' file=/u01/backup/GZGSNJ_LPS.dmp owner=GZGSNJ_LPS
exp \'/ as sysdba\' file=/u01/backup/GZGS_HZ_NZSC.dmp owner=GZGS_HZ_NZSC
exp \'/ as sysdba\' file=/u01/backup/GZGS_LINKAGE_HZ.dmp owner=GZGS_LINKAGE_HZ
exp \'/ as sysdba\' file=/u01/backup/DBTURN_GZGS.dmp owner=DBTURN_GZGS
exp \'/ as sysdba\' file=/u01/backup/GZGS_12315.dmp owner=GZGS_12315

