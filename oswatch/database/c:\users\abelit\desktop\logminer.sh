
    #!/bin/ksh

    export ORACLE_SID=gzgszxk1
    sqlplus / as sysdba <<!
    create or replace trigger on_logon_trigger
    after logon on database
    begin
    dbms_application_info.set_client_info(sys_context('userenv', 'ip_address'));
    end;
    /
    set echo off;
    set heading off;
    set line 100;
    set long 2000000000;
    set longchunksize 255;
    set wra on;
    set newpage none;
    set pagesize 0;
    set numwidth 12;
    set termout off;
    set trimout on;
    set trimspool on;
    set feedback off;
    set timing on;
    