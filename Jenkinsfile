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
                ./test/unit/mysql_class/Position_cmp.py
                ./test/unit/mysql_class/Server_init.py
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
