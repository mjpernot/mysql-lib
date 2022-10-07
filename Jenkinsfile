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
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install mysql-connector-python==8.0.22 --user
                /usr/bin/python2 ./test/unit/mysql_class/fetch_global_var.py
                /usr/bin/python2 ./test/unit/mysql_class/fetch_sys_var.py
                /usr/bin/python2 ./test/unit/mysql_class/flush_logs.py
                /usr/bin/python2 ./test/unit/mysql_class/show_master_stat.py
                /usr/bin/python2 ./test/unit/mysql_class/show_slave_hosts.py
                /usr/bin/python2 ./test/unit/mysql_class/show_slave_stat.py
                /usr/bin/python2 ./test/unit/mysql_class/slave_start.py
                /usr/bin/python2 ./test/unit/mysql_class/slave_stop.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_or.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_init.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_str.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_union.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_eq.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_ge.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_gt.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_le.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_lt.py
                /usr/bin/python2 ./test/unit/mysql_class/gtidset_ne.py
                /usr/bin/python2 ./test/unit/mysql_class/masterrep_connect.py
                /usr/bin/python2 ./test/unit/mysql_class/masterrep_init.py
                /usr/bin/python2 ./test/unit/mysql_class/masterrep_showslvhosts.py
                /usr/bin/python2 ./test/unit/mysql_class/masterrep_getloginfo.py
                /usr/bin/python2 ./test/unit/mysql_class/masterrep_updmststatus.py
                /usr/bin/python2 ./test/unit/mysql_class/position_cmp.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_fetchdodb.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_fetchigndb.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_getservid.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_init.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_showslvhosts.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_showslvstate.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_startslave.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_stopslave.py
                /usr/bin/python2 ./test/unit/mysql_class/rep_verify_srv_id.py
                /usr/bin/python2 ./test/unit/mysql_class/server_chg_db.py
                /usr/bin/python2 ./test/unit/mysql_class/server_connect.py
                /usr/bin/python2 ./test/unit/mysql_class/server_disconnect.py
                /usr/bin/python2 ./test/unit/mysql_class/server_fetchlogs.py
                /usr/bin/python2 ./test/unit/mysql_class/server_fetchmstrepcfg.py
                /usr/bin/python2 ./test/unit/mysql_class/server_fetchslvrepcfg.py
                /usr/bin/python2 ./test/unit/mysql_class/server_flushlogs.py
                /usr/bin/python2 ./test/unit/mysql_class/server_getname.py
                /usr/bin/python2 ./test/unit/mysql_class/server_init.py
                /usr/bin/python2 ./test/unit/mysql_class/server_is_connected.py
                /usr/bin/python2 ./test/unit/mysql_class/server_reconnect.py
                /usr/bin/python2 ./test/unit/mysql_class/server_set_pass_config.py
                /usr/bin/python2 ./test/unit/mysql_class/server_set_ssl_config.py
                /usr/bin/python2 ./test/unit/mysql_class/server_set_tls_config.py
                /usr/bin/python2 ./test/unit/mysql_class/server_setsrvbinlogcrc.py
                /usr/bin/python2 ./test/unit/mysql_class/server_setsrvgtid.py
                /usr/bin/python2 ./test/unit/mysql_class/server_setup_ssl.py
                /usr/bin/python2 ./test/unit/mysql_class/server_updlogstats.py
                /usr/bin/python2 ./test/unit/mysql_class/server_updmstrepstat.py
                /usr/bin/python2 ./test/unit/mysql_class/server_updsrvperf.py
                /usr/bin/python2 ./test/unit/mysql_class/server_updslvrepstat.py
                /usr/bin/python2 ./test/unit/mysql_class/server_updsrvstat.py
                /usr/bin/python2 ./test/unit/mysql_class/server_vertsql.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_connect.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_init.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_fetchdotbl.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_fetchigntbl.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_updslvstatus.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_geterrstat.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_getloginfo.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_getothers.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_getthrstat.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_gettime.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_isslaveup.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_isslverror.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_isslvrunning.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_showslvstate.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_startslave.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_stopslave.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_updslvstate.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_updslvtime.py
                /usr/bin/python2 ./test/unit/mysql_class/slaverep_updgtidpos.py
                /usr/bin/python2 ./test/unit/mysql_libs/_io_wait_chk.py
                /usr/bin/python2 ./test/unit/mysql_libs/_sql_wait_chk.py
                /usr/bin/python2 ./test/unit/mysql_libs/analyze_tbl.py
                /usr/bin/python2 ./test/unit/mysql_libs/change_master_to.py
                /usr/bin/python2 ./test/unit/mysql_libs/checksum.py
                /usr/bin/python2 ./test/unit/mysql_libs/check_tbl.py
                /usr/bin/python2 ./test/unit/mysql_libs/chg_slv_state.py
                /usr/bin/python2 ./test/unit/mysql_libs/create_instance.py
                /usr/bin/python2 ./test/unit/mysql_libs/disconnect.py
                /usr/bin/python2 ./test/unit/mysql_libs/fetch_db_dict.py
                /usr/bin/python2 ./test/unit/mysql_libs/fetch_logs.py
                /usr/bin/python2 ./test/unit/mysql_libs/fetch_tbl_dict.py
                /usr/bin/python2 ./test/unit/mysql_libs/optimize_tbl.py
                /usr/bin/python2 ./test/unit/mysql_libs/purge_bin_logs.py
                /usr/bin/python2 ./test/unit/mysql_libs/reset_master.py
                /usr/bin/python2 ./test/unit/mysql_libs/reset_slave.py
                /usr/bin/python2 ./test/unit/mysql_libs/select_wait_until.py
                /usr/bin/python2 ./test/unit/mysql_libs/create_slv_array.py
                /usr/bin/python2 ./test/unit/mysql_libs/crt_cmd.py
                /usr/bin/python2 ./test/unit/mysql_libs/fetch_slv.py
                /usr/bin/python2 ./test/unit/mysql_libs/find_name.py
                /usr/bin/python2 ./test/unit/mysql_libs/is_cfg_valid.py
                /usr/bin/python2 ./test/unit/mysql_libs/is_logs_synced.py
                /usr/bin/python2 ./test/unit/mysql_libs/is_rep_delay.py
                /usr/bin/python2 ./test/unit/mysql_libs/start_slave_until.py
                /usr/bin/python2 ./test/unit/mysql_libs/switch_to_master.py
                /usr/bin/python2 ./test/unit/mysql_libs/sync_delay.py
                /usr/bin/python2 ./test/unit/mysql_libs/sync_rep_slv.py
                /usr/bin/python2 ./test/unit/mysql_libs/wait_until.py
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
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}
