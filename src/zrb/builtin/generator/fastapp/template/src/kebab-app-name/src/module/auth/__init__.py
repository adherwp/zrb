from config import (
    app_enable_rpc_server, app_enable_message_consumer, app_enable_api,
    app_enable_auth_module
)
from component.log import logger
from component.app import app
from component.messagebus import consumer, publisher
from component.rpc import rpc_caller, rpc_server
from component.db_connection import engine
from helper.migration import migrate
from module.auth.component import Base
from module.auth.api import register_api
from module.auth.event import register_event
from module.auth.rpc import register_rpc


def migrate_auth():
    if not app_enable_auth_module:
        logger.info('🥪 Skip DB migration for "auth"')
        return
    logger.info('🥪 Perform DB migration for "auth"')
    migrate(engine=engine, Base=Base)


def register_auth():
    if not app_enable_auth_module:
        logger.info('🥪 Skip registering "auth"')
        return
    if app_enable_api:
        register_api(
            logger=logger,
            app=app,
            rpc_caller=rpc_caller,
            publisher=publisher
        )
    if app_enable_message_consumer:
        register_event(
            logger=logger,
            consumer=consumer,
            rpc_caller=rpc_caller,
            publisher=publisher
        )
    if app_enable_rpc_server:
        register_rpc(
            logger=logger,
            rpc_server=rpc_server,
            rpc_caller=rpc_caller,
            publisher=publisher
        )