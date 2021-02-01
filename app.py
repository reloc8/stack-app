#!/usr/bin/env python3

import os
from aws_cdk import core

from data_mining_stack import DataMiningStack
from data_processing_stack import DataProcessingStack, MongoDBConfiguration, AccessKeysConfiguration, \
    ImportedAssetsConfiguration

app = core.App()

dev_stack_data_mining = DataMiningStack(app, 'DataMiningStackDev', env=core.Environment(region='us-east-2'))
prod_stack_data_mining = DataMiningStack(app, 'DataMiningStackProd', env=core.Environment(region='eu-central-1'))

dev_stack_data_processing = DataProcessingStack(app, 'DataProcessingStackDev',
                                                env=core.Environment(region='us-east-2'),
                                                mongodb_config=MongoDBConfiguration(
                                                    uri=os.environ['DEV_MONGODB_URI'],
                                                    max_page_size='10',
                                                    database=os.environ['DEV_MONGODB_DATABASE'],
                                                    collection=''
                                                ),
                                                access_keys_config=AccessKeysConfiguration(
                                                    geocoding=os.environ['DEV_ACCESS_KEY_GEOCODING']
                                                ),
                                                imported_assets_config=ImportedAssetsConfiguration(
                                                    table_property=dev_stack_data_mining.table_property
                                                ))
prod_stack_data_processing = DataProcessingStack(app, 'DataProcessingStackProd',
                                                 env=core.Environment(region='eu-central-1'),
                                                 mongodb_config=MongoDBConfiguration(
                                                     uri=os.environ['PROD_MONGODB_URI'],
                                                     max_page_size='10',
                                                     database='',
                                                     collection=''
                                                 ),
                                                 access_keys_config=AccessKeysConfiguration(
                                                     geocoding=os.environ['PROD_ACCESS_KEY_GEOCODING']
                                                 ),
                                                 imported_assets_config=ImportedAssetsConfiguration(
                                                     table_property=prod_stack_data_mining.table_property
                                                 ))

app.synth()
