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
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock --user
                pip2 install mysql-connector-python --user
                ./test/unit/mysql_class/fetch_global_var.py
                ./test/unit/mysql_class/fetch_sys_var.py
                ./test/unit/mysql_class/flush_logs.py
                ./test/unit/mysql_class/show_master_stat.py
                ./test/unit/mysql_class/show_slave_hosts.py
                ./test/unit/mysql_class/show_slave_stat.py
                ./test/unit/mysql_class/slave_start.py
                ./test/unit/mysql_class/slave_stop.py
                ./test/unit/mysql_class/GTIDSet_init.py
                ./test/unit/mysql_class/GTIDSet_str.py
                ./test/unit/mysql_class/GTIDSet_union.py
                ./test/unit/mysql_class/GTIDSet_eq.py
                ./test/unit/mysql_class/GTIDSet_ge.py
                ./test/unit/mysql_class/GTIDSet_gt.py
                ./test/unit/mysql_class/GTIDSet_le.py
                ./test/unit/mysql_class/GTIDSet_lt.py
                ./test/unit/mysql_class/GTIDSet_ne.py
                ./test/unit/mysql_class/MasterRep_init.py
                ./test/unit/mysql_class/MasterRep_showslvhosts.py
                ./test/unit/mysql_class/MasterRep_getloginfo.py
                ./test/unit/mysql_class/MasterRep_updmststatus.py
                ./test/unit/mysql_class/Position_cmp.py
                ./test/unit/mysql_class/Rep_fetchdodb.py
                ./test/unit/mysql_class/Rep_fetchigndb.py
                ./test/unit/mysql_class/Rep_getservid.py
                ./test/unit/mysql_class/Rep_init.py
                ./test/unit/mysql_class/Rep_showslvhosts.py
                ./test/unit/mysql_class/Rep_showslvstate.py
                ./test/unit/mysql_class/Rep_startslave.py
                ./test/unit/mysql_class/Rep_stopslave.py
                ./test/unit/mysql_class/Server_init.py
                ./test/unit/mysql_class/Server_setsrvbinlogcrc.py
                ./test/unit/mysql_class/Server_setsrvgtid.py
                ./test/unit/mysql_class/Server_fetchmstrepcfg.py
                ./test/unit/mysql_class/Server_fetchslvrepcfg.py
                ./test/unit/mysql_class/Server_updmstrepstat.py
                ./test/unit/mysql_class/Server_updslvrepstat.py
                ./test/unit/mysql_class/Server_updsrvperf.py
                ./test/unit/mysql_class/Server_updsrvstat.py
                ./test/unit/mysql_class/Server_connect.py
                ./test/unit/mysql_class/Server_disconnect.py
                ./test/unit/mysql_class/Server_fetchlogs.py
                ./test/unit/mysql_class/Server_flushlogs.py
                ./test/unit/mysql_class/Server_vertsql.py
                ./test/unit/mysql_class/Server_updlogstats.py
                ./test/unit/mysql_class/SlaveRep_init.py
                ./test/unit/mysql_class/SlaveRep_updslvstatus.py
                ./test/unit/mysql_class/SlaveRep_geterrstat.py
                ./test/unit/mysql_class/SlaveRep_getloginfo.py
                ./test/unit/mysql_class/SlaveRep_getothers.py
                ./test/unit/mysql_class/SlaveRep_getthrstat.py
                ./test/unit/mysql_class/SlaveRep_gettime.py
                ./test/unit/mysql_class/SlaveRep_isslaveup.py
                ./test/unit/mysql_class/SlaveRep_isslverror.py
                ./test/unit/mysql_class/SlaveRep_isslvrunning.py
                ./test/unit/mysql_class/SlaveRep_showslvstate.py
                ./test/unit/mysql_class/SlaveRep_startslave.py
                ./test/unit/mysql_class/SlaveRep_stopslave.py
                ./test/unit/mysql_class/SlaveRep_updslvstate.py
                ./test/unit/mysql_class/SlaveRep_updslvtime.py
                ./test/unit/mysql_libs/analyze_tbl.py
                ./test/unit/mysql_libs/change_master_to.py
                ./test/unit/mysql_libs/checksum.py
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
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/mysql-lib/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
