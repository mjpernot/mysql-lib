pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install mysql-connector-python==8.0.16 --user
                ./test/unit/mysql_class/fetch_global_var.py
                ./test/unit/mysql_class/fetch_sys_var.py
                ./test/unit/mysql_class/flush_logs.py
                ./test/unit/mysql_class/show_master_stat.py
                ./test/unit/mysql_class/show_slave_hosts.py
                ./test/unit/mysql_class/show_slave_stat.py
                ./test/unit/mysql_class/slave_start.py
                ./test/unit/mysql_class/slave_stop.py
                ./test/unit/mysql_class/gtidset_or.py
                ./test/unit/mysql_class/gtidset_init.py
                ./test/unit/mysql_class/gtidset_str.py
                ./test/unit/mysql_class/gtidset_union.py
                ./test/unit/mysql_class/gtidset_eq.py
                ./test/unit/mysql_class/gtidset_ge.py
                ./test/unit/mysql_class/gtidset_gt.py
                ./test/unit/mysql_class/gtidset_le.py
                ./test/unit/mysql_class/gtidset_lt.py
                ./test/unit/mysql_class/gtidset_ne.py
                ./test/unit/mysql_class/masterrep_connect.py
                ./test/unit/mysql_class/masterrep_init.py
                ./test/unit/mysql_class/masterrep_showslvhosts.py
                ./test/unit/mysql_class/masterrep_getloginfo.py
                ./test/unit/mysql_class/masterrep_updmststatus.py
                ./test/unit/mysql_class/position_cmp.py
                ./test/unit/mysql_class/rep_fetchdodb.py
                ./test/unit/mysql_class/rep_fetchigndb.py
                ./test/unit/mysql_class/rep_getservid.py
                ./test/unit/mysql_class/rep_init.py
                ./test/unit/mysql_class/rep_showslvhosts.py
                ./test/unit/mysql_class/rep_showslvstate.py
                ./test/unit/mysql_class/rep_startslave.py
                ./test/unit/mysql_class/rep_stopslave.py
                ./test/unit/mysql_class/server_chg_db.py
                ./test/unit/mysql_class/server_connect.py
                ./test/unit/mysql_class/server_disconnect.py
                ./test/unit/mysql_class/server_fetchlogs.py
                ./test/unit/mysql_class/server_fetchmstrepcfg.py
                ./test/unit/mysql_class/server_fetchslvrepcfg.py
                ./test/unit/mysql_class/server_flushlogs.py
                ./test/unit/mysql_class/server_getname.py
                ./test/unit/mysql_class/server_init.py
                ./test/unit/mysql_class/server_is_connected.py
                ./test/unit/mysql_class/server_reconnect.py
                ./test/unit/mysql_class/server_set_pass_config.py
                ./test/unit/mysql_class/server_setsrvbinlogcrc.py
                ./test/unit/mysql_class/server_setsrvgtid.py
                ./test/unit/mysql_class/server_updlogstats.py
                ./test/unit/mysql_class/server_updmstrepstat.py
                ./test/unit/mysql_class/server_updsrvperf.py
                ./test/unit/mysql_class/server_updslvrepstat.py
                ./test/unit/mysql_class/server_updsrvstat.py
                ./test/unit/mysql_class/server_vertsql.py
                ./test/unit/mysql_class/slaverep_connect.py
                ./test/unit/mysql_class/slaverep_init.py
                ./test/unit/mysql_class/slaverep_fetchdotbl.py
                ./test/unit/mysql_class/slaverep_fetchigntbl.py
                ./test/unit/mysql_class/slaverep_updslvstatus.py
                ./test/unit/mysql_class/slaverep_geterrstat.py
                ./test/unit/mysql_class/slaverep_getloginfo.py
                ./test/unit/mysql_class/slaverep_getothers.py
                ./test/unit/mysql_class/slaverep_getthrstat.py
                ./test/unit/mysql_class/slaverep_gettime.py
                ./test/unit/mysql_class/slaverep_isslaveup.py
                ./test/unit/mysql_class/slaverep_isslverror.py
                ./test/unit/mysql_class/slaverep_isslvrunning.py
                ./test/unit/mysql_class/slaverep_showslvstate.py
                ./test/unit/mysql_class/slaverep_startslave.py
                ./test/unit/mysql_class/slaverep_stopslave.py
                ./test/unit/mysql_class/slaverep_updslvstate.py
                ./test/unit/mysql_class/slaverep_updslvtime.py
                ./test/unit/mysql_class/slaverep_updgtidpos.py
                ./test/unit/mysql_libs/_io_wait_chk.py
                ./test/unit/mysql_libs/_sql_wait_chk.py
                ./test/unit/mysql_libs/analyze_tbl.py
                ./test/unit/mysql_libs/change_master_to.py
                ./test/unit/mysql_libs/checksum.py
                ./test/unit/mysql_libs/check_tbl.py
                ./test/unit/mysql_libs/chg_slv_state.py
                ./test/unit/mysql_libs/create_instance.py
                ./test/unit/mysql_libs/disconnect.py
                ./test/unit/mysql_libs/fetch_db_dict.py
                ./test/unit/mysql_libs/fetch_logs.py
                ./test/unit/mysql_libs/fetch_tbl_dict.py
                ./test/unit/mysql_libs/optimize_tbl.py
                ./test/unit/mysql_libs/purge_bin_logs.py
                ./test/unit/mysql_libs/reset_master.py
                ./test/unit/mysql_libs/reset_slave.py
                ./test/unit/mysql_libs/select_wait_until.py
                ./test/unit/mysql_libs/create_slv_array.py
                ./test/unit/mysql_libs/crt_cmd.py
                ./test/unit/mysql_libs/crt_srv_inst.py
                ./test/unit/mysql_libs/fetch_slv.py
                ./test/unit/mysql_libs/find_name.py
                ./test/unit/mysql_libs/is_cfg_valid.py
                ./test/unit/mysql_libs/is_logs_synced.py
                ./test/unit/mysql_libs/is_rep_delay.py
                ./test/unit/mysql_libs/start_slave_until.py
                ./test/unit/mysql_libs/switch_to_master.py
                ./test/unit/mysql_libs/sync_delay.py
                ./test/unit/mysql_libs/sync_rep_slv.py
                ./test/unit/mysql_libs/wait_until.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/mysql-lib/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
