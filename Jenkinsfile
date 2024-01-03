def qa_stage_run=false


pipeline {

    agent any
    stages {
        stage ('checkout') {
                    steps {
                        sh 'mkdir -p deployments'
                        dir("build")
                        {
                            git branch: "main",
                            credentialsId: "raj-epam",
                            url: 'https://github.com/raj-epam/app-testcase1-deploy.git'
                        }
                    }
                }

        //     }
        // }
    //stage ("Scan Code")
    //Docker Image Build
    stage ('Build') {
            steps {
                dir("build")
                {
                    sh 'docker build -t dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER} .'
                }
            }
        }
    stage('SYNK Scan') {
        steps {
            dir("build")
            {
                snykSecurity monitorProjectOnBuild: false, organisation: 'raj-epam', projectName: 'python_demo-FE', severity: 'critical', snykInstallation: 'snyk', snykTokenId: 'org-synk-credentials', targetFile: './Dockerfile'
                def variable = sh(
                    script:'snyk container test dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}  --file=./Dockerfile --json-file-output=vulnerabilities.json', 
                    returnStatus: true
                )
                sh 'snyk-filter -i vulnerabilities.json -f exploitable_cvss_9.yml'

                echo "error code = ${variable}"
            }
        }
    }

        // stage ('Push') {
        //     steps {
        //         dir("build")
        //         {
        //             sh 'docker push dhlawowacr.azurecr.io/pywebapp:${BUILD_NUMBER}'
        //         }
        //     }
        // }

        post {
            // Clean after build
            always {
                cleanWs(cleanWhenNotBuilt: false,
                        deleteDirs: true,
                        disableDeferredWipeout: true,
                        notFailBuild: true,
                        patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
                                [pattern: '.propsfile', type: 'EXCLUDE']])
            }
    }


}