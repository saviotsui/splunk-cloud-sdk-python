# coding: utf-8

# flake8: noqa

# Copyright © 2019 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# [http://www.apache.org/licenses/LICENSE-2.0]
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

############# This file is auto-generated.  Do not edit! #############

"""
    SDC Service: Machine Learning

    Use the Machine Learning service in Splunk Cloud Services to deliver resource intensive machine learning workloads. The Machine Learning service covers model experimentation, training, inference, validation, scoring, and serving.

    OpenAPI spec version: v2beta1.1 (recommended default)
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import apis into sdk package
from splunk_sdk.ml.v2beta1.gen_machine_learning_api import MachineLearning

# import models into sdk package
from splunk_sdk.ml.v2beta1.gen_models import WorkflowValidationOption, \
    CrossValidation, \
    DeploymentSpec, \
    Error, \
    OutputDataDestination, \
    Events, \
    ExecutorErrors, \
    ExecutorLogs, \
    Fields, \
    Task, \
    FitTask, \
    InputDataSource, \
    InputData, \
    InputStreamSource, \
    InputStream, \
    KafkaInput, \
    OutputStreamDestination, \
    KafkaOutput, \
    OutputData, \
    OutputStream, \
    RawData, \
    SPL, \
    ScoreReport, \
    Score, \
    TaskSummary, \
    WorkflowValidationScore, \
    TrainTestScore, \
    TrainTestSplit, \
    Workflow, \
    WorkflowBuildValidationOption, \
    WorkflowBuildValidationScore, \
    WorkflowBuild, \
    WorkflowManagerErrors, \
    WorkflowBuildError, \
    WorkflowManagerLogs, \
    WorkflowBuildLog, \
    WorkflowDeployment, \
    WorkflowDeploymentError, \
    WorkflowDeploymentLog, \
    WorkflowInference, \
    WorkflowRun, \
    WorkflowRunError, \
    WorkflowRunLog, \
    WorkflowStreamDeployment, \
    WorkflowsGetResponse
