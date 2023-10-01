'''setup file for behave'''
# pylint: disable=consider-using-f-string,too-many-public-methods,unused-argument,wildcard-import,too-many-branches,unused-wildcard-import

# -*- coding: UTF-8 -*-
import requests
from behave import *
from settings import default_headers, JIRA_PROJECT_ABBR, log


def get_jira_number_from_tags(context):
    '''
       Gets JIRA Key & Number for adding to skip messages on tests 
       being skipped due to know issues
    '''
    for tag in context.tags:
        if JIRA_PROJECT_ABBR in tag:
            return tag
    return None

def before_all(context):
    '''leaving setup function, currently unused'''


def after_all(context):
    '''leaving cleanup function, currently unused'''


def before_feature(context, feature):
    '''Used to add environment to feature name if behave is set to server user'''


def after_feature(context, feature):
    '''leaving cleanup function, currently unused'''


def before_scenario(context, scenario):
    '''Setup function, works off behave tags to skip tests only supported on certain scenarios'''
    if 'skip' in context.tags:
        jira_number = get_jira_number_from_tags(context)
        scenario.skip("\n\tSkipping tests until %s is fixed" % jira_number)
        return
    context.session = session = requests.Session()
    context.session.headers.update(default_headers)


def after_scenario(context, scenario):
    '''Quits chromedriver at end of scernario when usng chrome'''
