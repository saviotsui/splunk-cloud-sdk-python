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
    SDC Service: Action Service

    With the Splunk Cloud Action service, you can receive incoming trigger events and use pre-defined action templates to turn these events into meaningful actions. 

    OpenAPI spec version: v2alpha1.8 
    Generated by: https://openapi-generator.tech
"""


from datetime import datetime
from typing import List, Dict
from splunk_sdk.common.sscmodel import SSCModel
from splunk_sdk.base_client import dictify, inflate
from enum import Enum



class Action(SSCModel):

    from_dict_handlers = dict()
    @staticmethod
    def _from_dict(model: dict) -> "Action":

        def default_handler(model: dict) -> "Action":
            instance = Action.__new__(Action)
            instance._attrs = model
            return instance

        kind = model['kind']
        handler = Action.from_dict_handlers.get(kind, default_handler)
        return handler(model)

    def __init__(self, created_at: "datetime" = None, created_by: "str" = None, name: "str" = None, updated_at: "datetime" = None, updated_by: "str" = None, **extra):
        """Action"""

        self._attrs = dict()
        if name is not None:
            self._attrs["name"] = name
        if created_at is not None:
            self._attrs["createdAt"] = created_at
        if created_by is not None:
            self._attrs["createdBy"] = created_by
        if updated_at is not None:
            self._attrs["updatedAt"] = updated_at
        if updated_by is not None:
            self._attrs["updatedBy"] = updated_by
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def name(self) -> "str":
        """ Gets the name of this Action.
        The name of the action, as one or more identifier strings separated by periods. Each identifier string consists of lowercase letters, digits, and underscores, and cannot start with a digit.
        """
        return self._attrs.get("name")

    @name.setter
    def name(self, name: "str"):
        """Sets the name of this Action.

        The name of the action, as one or more identifier strings separated by periods. Each identifier string consists of lowercase letters, digits, and underscores, and cannot start with a digit.

        :param name: The name of this Action.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._attrs["name"] = name

    @property
    def created_at(self) -> "datetime":
        """ Gets the created_at of this Action.
        The date and time this action template was created (ISO-8601 date/time with zone).
        """
        return self._attrs.get("createdAt")

    @created_at.setter
    def created_at(self, created_at: "datetime"):
        """Sets the created_at of this Action.

        The date and time this action template was created (ISO-8601 date/time with zone).

        :param created_at: The created_at of this Action.
        :type: datetime
        """
        self._attrs["createdAt"] = created_at

    @property
    def created_by(self) -> "str":
        """ Gets the created_by of this Action.
        The principal that created this action template.
        """
        return self._attrs.get("createdBy")

    @created_by.setter
    def created_by(self, created_by: "str"):
        """Sets the created_by of this Action.

        The principal that created this action template.

        :param created_by: The created_by of this Action.
        :type: str
        """
        self._attrs["createdBy"] = created_by

    @property
    def updated_at(self) -> "datetime":
        """ Gets the updated_at of this Action.
        The date and time this action template was updated (ISO-8601 date/time with zone).
        """
        return self._attrs.get("updatedAt")

    @updated_at.setter
    def updated_at(self, updated_at: "datetime"):
        """Sets the updated_at of this Action.

        The date and time this action template was updated (ISO-8601 date/time with zone).

        :param updated_at: The updated_at of this Action.
        :type: datetime
        """
        self._attrs["updatedAt"] = updated_at

    @property
    def updated_by(self) -> "str":
        """ Gets the updated_by of this Action.
        The principal that updated this action template.
        """
        return self._attrs.get("updatedBy")

    @updated_by.setter
    def updated_by(self, updated_by: "str"):
        """Sets the updated_by of this Action.

        The principal that updated this action template.

        :param updated_by: The updated_by of this Action.
        :type: str
        """
        self._attrs["updatedBy"] = updated_by

    def to_dict(self):
        raise NotImplementedError()


class ActionKind(str, Enum):
    WEBHOOK = "webhook"
    EMAIL = "email"

    @staticmethod
    def from_value(value: str):
        if value == "webhook":
            return ActionKind.WEBHOOK
        if value == "email":
            return ActionKind.EMAIL


class ActionMutable(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "ActionMutable":
        instance = ActionMutable.__new__(ActionMutable)
        instance._attrs = model
        return instance

    def __init__(self, **extra):
        """ActionMutable"""

        self._attrs = dict()
        for k, v in extra.items():
            self._attrs[k] = v

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class EmailAction(Action):

    @staticmethod
    def _from_dict(model: dict) -> "EmailAction":
        instance = EmailAction.__new__(EmailAction)
        instance._attrs = model
        return instance

    def __init__(self, name: "str", addresses: "List[str]" = None, body: "str" = None, body_plain_text: "str" = None, created_at: "datetime" = None, created_by: "str" = None, from_name: "str" = None, members: "List[str]" = None, subject: "str" = None, title: "str" = None, updated_at: "datetime" = None, updated_by: "str" = None, **extra):
        """EmailAction"""

        self._attrs = dict()
        self._attrs["kind"] = "email" 
        if name is not None:
            self._attrs["name"] = name
        if addresses is not None:
            self._attrs["addresses"] = addresses
        if body is not None:
            self._attrs["body"] = body
        if body_plain_text is not None:
            self._attrs["bodyPlainText"] = body_plain_text
        if created_at is not None:
            self._attrs["createdAt"] = created_at
        if created_by is not None:
            self._attrs["createdBy"] = created_by
        if from_name is not None:
            self._attrs["fromName"] = from_name
        if members is not None:
            self._attrs["members"] = members
        if subject is not None:
            self._attrs["subject"] = subject
        if title is not None:
            self._attrs["title"] = title
        if updated_at is not None:
            self._attrs["updatedAt"] = updated_at
        if updated_by is not None:
            self._attrs["updatedBy"] = updated_by
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def kind(self) -> str:
        return "email"


    @property
    def name(self) -> "str":
        """ Gets the name of this EmailAction.
        The name of the action, as one or more identifier strings separated by periods. Each identifier string consists of lowercase letters, digits, and underscores, and cannot start with a digit.
        """
        return self._attrs.get("name")

    @name.setter
    def name(self, name: "str"):
        """Sets the name of this EmailAction.

        The name of the action, as one or more identifier strings separated by periods. Each identifier string consists of lowercase letters, digits, and underscores, and cannot start with a digit.

        :param name: The name of this EmailAction.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._attrs["name"] = name

    @property
    def addresses(self) -> "List[str]":
        """ Gets the addresses of this EmailAction.
        An array of email addresses to include as recipients. Requires a special permission set for use. Please DO NOT include actual bouncing emails in automated testing. 
        """
        return self._attrs.get("addresses")

    @addresses.setter
    def addresses(self, addresses: "List[str]"):
        """Sets the addresses of this EmailAction.

        An array of email addresses to include as recipients. Requires a special permission set for use. Please DO NOT include actual bouncing emails in automated testing. 

        :param addresses: The addresses of this EmailAction.
        :type: List[str]
        """
        self._attrs["addresses"] = addresses

    @property
    def body(self) -> "str":
        """ Gets the body of this EmailAction.
        HTML content to send as the body of the email. You can use a template in this field.
        """
        return self._attrs.get("body")

    @body.setter
    def body(self, body: "str"):
        """Sets the body of this EmailAction.

        HTML content to send as the body of the email. You can use a template in this field.

        :param body: The body of this EmailAction.
        :type: str
        """
        self._attrs["body"] = body

    @property
    def body_plain_text(self) -> "str":
        """ Gets the body_plain_text of this EmailAction.
        Optional text to send as the text/plain part of the email. If this field is not set for an email action, the Action service converts the value from the body field to text and sends that as the text/plain part when triggering the action. You can use a template in this field.
        """
        return self._attrs.get("bodyPlainText")

    @body_plain_text.setter
    def body_plain_text(self, body_plain_text: "str"):
        """Sets the body_plain_text of this EmailAction.

        Optional text to send as the text/plain part of the email. If this field is not set for an email action, the Action service converts the value from the body field to text and sends that as the text/plain part when triggering the action. You can use a template in this field.

        :param body_plain_text: The body_plain_text of this EmailAction.
        :type: str
        """
        self._attrs["bodyPlainText"] = body_plain_text

    @property
    def created_at(self) -> "datetime":
        """ Gets the created_at of this EmailAction.
        The date and time this action template was created (ISO-8601 date/time with zone).
        """
        return self._attrs.get("createdAt")

    @created_at.setter
    def created_at(self, created_at: "datetime"):
        """Sets the created_at of this EmailAction.

        The date and time this action template was created (ISO-8601 date/time with zone).

        :param created_at: The created_at of this EmailAction.
        :type: datetime
        """
        self._attrs["createdAt"] = created_at

    @property
    def created_by(self) -> "str":
        """ Gets the created_by of this EmailAction.
        The principal that created this action template.
        """
        return self._attrs.get("createdBy")

    @created_by.setter
    def created_by(self, created_by: "str"):
        """Sets the created_by of this EmailAction.

        The principal that created this action template.

        :param created_by: The created_by of this EmailAction.
        :type: str
        """
        self._attrs["createdBy"] = created_by

    @property
    def from_name(self) -> "str":
        """ Gets the from_name of this EmailAction.
        Optional text providing a human-friendly name for the sender. Must be less than or equal to 81 characters. You can use a template in this field.
        """
        return self._attrs.get("fromName")

    @from_name.setter
    def from_name(self, from_name: "str"):
        """Sets the from_name of this EmailAction.

        Optional text providing a human-friendly name for the sender. Must be less than or equal to 81 characters. You can use a template in this field.

        :param from_name: The from_name of this EmailAction.
        :type: str
        """
        self._attrs["fromName"] = from_name

    @property
    def members(self) -> "List[str]":
        """ Gets the members of this EmailAction.
        An array of tenant member names, whose profile email addresses will be included as recipients.
        """
        return self._attrs.get("members")

    @members.setter
    def members(self, members: "List[str]"):
        """Sets the members of this EmailAction.

        An array of tenant member names, whose profile email addresses will be included as recipients.

        :param members: The members of this EmailAction.
        :type: List[str]
        """
        self._attrs["members"] = members

    @property
    def subject(self) -> "str":
        """ Gets the subject of this EmailAction.
        The subject of the email. You can use a template in this field.
        """
        return self._attrs.get("subject")

    @subject.setter
    def subject(self, subject: "str"):
        """Sets the subject of this EmailAction.

        The subject of the email. You can use a template in this field.

        :param subject: The subject of this EmailAction.
        :type: str
        """
        self._attrs["subject"] = subject

    @property
    def title(self) -> "str":
        """ Gets the title of this EmailAction.
        A human-readable title for the action. Must be less than or equal to 128 characters.
        """
        return self._attrs.get("title")

    @title.setter
    def title(self, title: "str"):
        """Sets the title of this EmailAction.

        A human-readable title for the action. Must be less than or equal to 128 characters.

        :param title: The title of this EmailAction.
        :type: str
        """
        self._attrs["title"] = title

    @property
    def updated_at(self) -> "datetime":
        """ Gets the updated_at of this EmailAction.
        The date and time this action template was updated (ISO-8601 date/time with zone).
        """
        return self._attrs.get("updatedAt")

    @updated_at.setter
    def updated_at(self, updated_at: "datetime"):
        """Sets the updated_at of this EmailAction.

        The date and time this action template was updated (ISO-8601 date/time with zone).

        :param updated_at: The updated_at of this EmailAction.
        :type: datetime
        """
        self._attrs["updatedAt"] = updated_at

    @property
    def updated_by(self) -> "str":
        """ Gets the updated_by of this EmailAction.
        The principal that updated this action template.
        """
        return self._attrs.get("updatedBy")

    @updated_by.setter
    def updated_by(self, updated_by: "str"):
        """Sets the updated_by of this EmailAction.

        The principal that updated this action template.

        :param updated_by: The updated_by of this EmailAction.
        :type: str
        """
        self._attrs["updatedBy"] = updated_by

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


Action.from_dict_handlers["email"] = EmailAction._from_dict



class EmailActionMutable(ActionMutable):

    @staticmethod
    def _from_dict(model: dict) -> "EmailActionMutable":
        instance = EmailActionMutable.__new__(EmailActionMutable)
        instance._attrs = model
        return instance

    def __init__(self, addresses: "List[str]" = None, body: "str" = None, body_plain_text: "str" = None, from_name: "str" = None, members: "List[str]" = None, subject: "str" = None, title: "str" = None, **extra):
        """EmailActionMutable"""

        self._attrs = dict()
        if addresses is not None:
            self._attrs["addresses"] = addresses
        if body is not None:
            self._attrs["body"] = body
        if body_plain_text is not None:
            self._attrs["bodyPlainText"] = body_plain_text
        if from_name is not None:
            self._attrs["fromName"] = from_name
        if members is not None:
            self._attrs["members"] = members
        if subject is not None:
            self._attrs["subject"] = subject
        if title is not None:
            self._attrs["title"] = title
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def addresses(self) -> "List[str]":
        """ Gets the addresses of this EmailActionMutable.
        An array of email addresses to include as recipients. Requires a special permission set for use. Please DO NOT include actual bouncing emails in automated testing. 
        """
        return self._attrs.get("addresses")

    @addresses.setter
    def addresses(self, addresses: "List[str]"):
        """Sets the addresses of this EmailActionMutable.

        An array of email addresses to include as recipients. Requires a special permission set for use. Please DO NOT include actual bouncing emails in automated testing. 

        :param addresses: The addresses of this EmailActionMutable.
        :type: List[str]
        """
        self._attrs["addresses"] = addresses

    @property
    def body(self) -> "str":
        """ Gets the body of this EmailActionMutable.
        HTML content to send as the body of the email. You can use a template in this field.
        """
        return self._attrs.get("body")

    @body.setter
    def body(self, body: "str"):
        """Sets the body of this EmailActionMutable.

        HTML content to send as the body of the email. You can use a template in this field.

        :param body: The body of this EmailActionMutable.
        :type: str
        """
        self._attrs["body"] = body

    @property
    def body_plain_text(self) -> "str":
        """ Gets the body_plain_text of this EmailActionMutable.
        Optional text to send as the text/plain part of the email. If this field is not set for an email action, the Action service converts the value from the body field to text and sends that as the text/plain part when triggering the action. You can use a template in this field.
        """
        return self._attrs.get("bodyPlainText")

    @body_plain_text.setter
    def body_plain_text(self, body_plain_text: "str"):
        """Sets the body_plain_text of this EmailActionMutable.

        Optional text to send as the text/plain part of the email. If this field is not set for an email action, the Action service converts the value from the body field to text and sends that as the text/plain part when triggering the action. You can use a template in this field.

        :param body_plain_text: The body_plain_text of this EmailActionMutable.
        :type: str
        """
        self._attrs["bodyPlainText"] = body_plain_text

    @property
    def from_name(self) -> "str":
        """ Gets the from_name of this EmailActionMutable.
        Optional text providing a human-friendly name for the sender. Must be less than or equal to 81 characters. You can use a template in this field.
        """
        return self._attrs.get("fromName")

    @from_name.setter
    def from_name(self, from_name: "str"):
        """Sets the from_name of this EmailActionMutable.

        Optional text providing a human-friendly name for the sender. Must be less than or equal to 81 characters. You can use a template in this field.

        :param from_name: The from_name of this EmailActionMutable.
        :type: str
        """
        self._attrs["fromName"] = from_name

    @property
    def members(self) -> "List[str]":
        """ Gets the members of this EmailActionMutable.
        An array of tenant member names, whose profile email addresses will be included as recipients.
        """
        return self._attrs.get("members")

    @members.setter
    def members(self, members: "List[str]"):
        """Sets the members of this EmailActionMutable.

        An array of tenant member names, whose profile email addresses will be included as recipients.

        :param members: The members of this EmailActionMutable.
        :type: List[str]
        """
        self._attrs["members"] = members

    @property
    def subject(self) -> "str":
        """ Gets the subject of this EmailActionMutable.
        The subject of the email. You can use a template in this field.
        """
        return self._attrs.get("subject")

    @subject.setter
    def subject(self, subject: "str"):
        """Sets the subject of this EmailActionMutable.

        The subject of the email. You can use a template in this field.

        :param subject: The subject of this EmailActionMutable.
        :type: str
        """
        self._attrs["subject"] = subject

    @property
    def title(self) -> "str":
        """ Gets the title of this EmailActionMutable.
        A human-readable title for the action. Must be less than or equal to 128 characters.
        """
        return self._attrs.get("title")

    @title.setter
    def title(self, title: "str"):
        """Sets the title of this EmailActionMutable.

        A human-readable title for the action. Must be less than or equal to 128 characters.

        :param title: The title of this EmailActionMutable.
        :type: str
        """
        self._attrs["title"] = title

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class PublicWebhookKey(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "PublicWebhookKey":
        instance = PublicWebhookKey.__new__(PublicWebhookKey)
        instance._attrs = model
        return instance

    def __init__(self, key: "str", **extra):
        """PublicWebhookKey"""

        self._attrs = dict()
        if key is not None:
            self._attrs["key"] = key
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def key(self) -> "str":
        """ Gets the key of this PublicWebhookKey.
        A PEM-formatted, ASN.1 DER-encoded PKCS#1 key.
        """
        return self._attrs.get("key")

    @key.setter
    def key(self, key: "str"):
        """Sets the key of this PublicWebhookKey.

        A PEM-formatted, ASN.1 DER-encoded PKCS#1 key.

        :param key: The key of this PublicWebhookKey.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")
        self._attrs["key"] = key

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class ServiceError(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "ServiceError":
        instance = ServiceError.__new__(ServiceError)
        instance._attrs = model
        return instance

    def __init__(self, code: "str", message: "str", details: "object" = None, more_info: "str" = None, **extra):
        """ServiceError"""

        self._attrs = dict()
        if code is not None:
            self._attrs["code"] = code
        if message is not None:
            self._attrs["message"] = message
        if details is not None:
            self._attrs["details"] = details
        if more_info is not None:
            self._attrs["moreInfo"] = more_info
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def code(self) -> "str":
        """ Gets the code of this ServiceError.
        """
        return self._attrs.get("code")

    @code.setter
    def code(self, code: "str"):
        """Sets the code of this ServiceError.


        :param code: The code of this ServiceError.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")
        self._attrs["code"] = code

    @property
    def message(self) -> "str":
        """ Gets the message of this ServiceError.
        """
        return self._attrs.get("message")

    @message.setter
    def message(self, message: "str"):
        """Sets the message of this ServiceError.


        :param message: The message of this ServiceError.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")
        self._attrs["message"] = message

    @property
    def details(self) -> "dict":
        """ Gets the details of this ServiceError.
        """
        return self._attrs.get("details")

    @details.setter
    def details(self, details: "dict"):
        """Sets the details of this ServiceError.


        :param details: The details of this ServiceError.
        :type: object
        """
        self._attrs["details"] = details

    @property
    def more_info(self) -> "str":
        """ Gets the more_info of this ServiceError.
        """
        return self._attrs.get("moreInfo")

    @more_info.setter
    def more_info(self, more_info: "str"):
        """Sets the more_info of this ServiceError.


        :param more_info: The more_info of this ServiceError.
        :type: str
        """
        self._attrs["moreInfo"] = more_info

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class WebhookAction(Action):

    @staticmethod
    def _from_dict(model: dict) -> "WebhookAction":
        instance = WebhookAction.__new__(WebhookAction)
        instance._attrs = model
        return instance

    def __init__(self, name: "str", created_at: "datetime" = None, created_by: "str" = None, title: "str" = None, updated_at: "datetime" = None, updated_by: "str" = None, webhook_headers: "Dict[str, List[str]]" = None, webhook_payload: "str" = None, webhook_url: "str" = None, **extra):
        """WebhookAction"""

        self._attrs = dict()
        self._attrs["kind"] = "webhook" 
        if name is not None:
            self._attrs["name"] = name
        if created_at is not None:
            self._attrs["createdAt"] = created_at
        if created_by is not None:
            self._attrs["createdBy"] = created_by
        if title is not None:
            self._attrs["title"] = title
        if updated_at is not None:
            self._attrs["updatedAt"] = updated_at
        if updated_by is not None:
            self._attrs["updatedBy"] = updated_by
        if webhook_headers is not None:
            self._attrs["webhookHeaders"] = webhook_headers
        if webhook_payload is not None:
            self._attrs["webhookPayload"] = webhook_payload
        if webhook_url is not None:
            self._attrs["webhookUrl"] = webhook_url
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def kind(self) -> str:
        return "webhook"


    @property
    def name(self) -> "str":
        """ Gets the name of this WebhookAction.
        The name of the action, as one or more identifier strings separated by periods. Each identifier string consists of lowercase letters, digits, and underscores, and cannot start with a digit.
        """
        return self._attrs.get("name")

    @name.setter
    def name(self, name: "str"):
        """Sets the name of this WebhookAction.

        The name of the action, as one or more identifier strings separated by periods. Each identifier string consists of lowercase letters, digits, and underscores, and cannot start with a digit.

        :param name: The name of this WebhookAction.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._attrs["name"] = name

    @property
    def created_at(self) -> "datetime":
        """ Gets the created_at of this WebhookAction.
        The date and time this action template was created (ISO-8601 date/time with zone).
        """
        return self._attrs.get("createdAt")

    @created_at.setter
    def created_at(self, created_at: "datetime"):
        """Sets the created_at of this WebhookAction.

        The date and time this action template was created (ISO-8601 date/time with zone).

        :param created_at: The created_at of this WebhookAction.
        :type: datetime
        """
        self._attrs["createdAt"] = created_at

    @property
    def created_by(self) -> "str":
        """ Gets the created_by of this WebhookAction.
        The principal that created this action template.
        """
        return self._attrs.get("createdBy")

    @created_by.setter
    def created_by(self, created_by: "str"):
        """Sets the created_by of this WebhookAction.

        The principal that created this action template.

        :param created_by: The created_by of this WebhookAction.
        :type: str
        """
        self._attrs["createdBy"] = created_by

    @property
    def title(self) -> "str":
        """ Gets the title of this WebhookAction.
        A human-readable title for the action. Must be less than 128 characters.
        """
        return self._attrs.get("title")

    @title.setter
    def title(self, title: "str"):
        """Sets the title of this WebhookAction.

        A human-readable title for the action. Must be less than 128 characters.

        :param title: The title of this WebhookAction.
        :type: str
        """
        self._attrs["title"] = title

    @property
    def updated_at(self) -> "datetime":
        """ Gets the updated_at of this WebhookAction.
        The date and time this action template was updated (ISO-8601 date/time with zone).
        """
        return self._attrs.get("updatedAt")

    @updated_at.setter
    def updated_at(self, updated_at: "datetime"):
        """Sets the updated_at of this WebhookAction.

        The date and time this action template was updated (ISO-8601 date/time with zone).

        :param updated_at: The updated_at of this WebhookAction.
        :type: datetime
        """
        self._attrs["updatedAt"] = updated_at

    @property
    def updated_by(self) -> "str":
        """ Gets the updated_by of this WebhookAction.
        The principal that updated this action template.
        """
        return self._attrs.get("updatedBy")

    @updated_by.setter
    def updated_by(self, updated_by: "str"):
        """Sets the updated_by of this WebhookAction.

        The principal that updated this action template.

        :param updated_by: The updated_by of this WebhookAction.
        :type: str
        """
        self._attrs["updatedBy"] = updated_by

    @property
    def webhook_headers(self) -> "Dict[str, List[str]]":
        """ Gets the webhook_headers of this WebhookAction.
        """
        return self._attrs.get("webhookHeaders")

    @webhook_headers.setter
    def webhook_headers(self, webhook_headers: "Dict[str, List[str]]"):
        """Sets the webhook_headers of this WebhookAction.


        :param webhook_headers: The webhook_headers of this WebhookAction.
        :type: Dict[str, List[str]]
        """
        self._attrs["webhookHeaders"] = webhook_headers

    @property
    def webhook_payload(self) -> "str":
        """ Gets the webhook_payload of this WebhookAction.
        The (possibly) templated payload body, which is POSTed to the webhookUrl. 
        """
        return self._attrs.get("webhookPayload")

    @webhook_payload.setter
    def webhook_payload(self, webhook_payload: "str"):
        """Sets the webhook_payload of this WebhookAction.

        The (possibly) templated payload body, which is POSTed to the webhookUrl. 

        :param webhook_payload: The webhook_payload of this WebhookAction.
        :type: str
        """
        self._attrs["webhookPayload"] = webhook_payload

    @property
    def webhook_url(self) -> "str":
        """ Gets the webhook_url of this WebhookAction.
        Only HTTPS is allowed. 
        """
        return self._attrs.get("webhookUrl")

    @webhook_url.setter
    def webhook_url(self, webhook_url: "str"):
        """Sets the webhook_url of this WebhookAction.

        Only HTTPS is allowed. 

        :param webhook_url: The webhook_url of this WebhookAction.
        :type: str
        """
        self._attrs["webhookUrl"] = webhook_url

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


Action.from_dict_handlers["webhook"] = WebhookAction._from_dict



class WebhookActionMutable(ActionMutable):

    @staticmethod
    def _from_dict(model: dict) -> "WebhookActionMutable":
        instance = WebhookActionMutable.__new__(WebhookActionMutable)
        instance._attrs = model
        return instance

    def __init__(self, title: "str" = None, webhook_headers: "Dict[str, List[str]]" = None, webhook_payload: "str" = None, webhook_url: "str" = None, **extra):
        """WebhookActionMutable"""

        self._attrs = dict()
        if title is not None:
            self._attrs["title"] = title
        if webhook_headers is not None:
            self._attrs["webhookHeaders"] = webhook_headers
        if webhook_payload is not None:
            self._attrs["webhookPayload"] = webhook_payload
        if webhook_url is not None:
            self._attrs["webhookUrl"] = webhook_url
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def title(self) -> "str":
        """ Gets the title of this WebhookActionMutable.
        A human-readable title for the action. Must be less than 128 characters.
        """
        return self._attrs.get("title")

    @title.setter
    def title(self, title: "str"):
        """Sets the title of this WebhookActionMutable.

        A human-readable title for the action. Must be less than 128 characters.

        :param title: The title of this WebhookActionMutable.
        :type: str
        """
        self._attrs["title"] = title

    @property
    def webhook_headers(self) -> "Dict[str, List[str]]":
        """ Gets the webhook_headers of this WebhookActionMutable.
        """
        return self._attrs.get("webhookHeaders")

    @webhook_headers.setter
    def webhook_headers(self, webhook_headers: "Dict[str, List[str]]"):
        """Sets the webhook_headers of this WebhookActionMutable.


        :param webhook_headers: The webhook_headers of this WebhookActionMutable.
        :type: Dict[str, List[str]]
        """
        self._attrs["webhookHeaders"] = webhook_headers

    @property
    def webhook_payload(self) -> "str":
        """ Gets the webhook_payload of this WebhookActionMutable.
        The (possibly) templated payload body, which is POSTed to the webhookUrl. 
        """
        return self._attrs.get("webhookPayload")

    @webhook_payload.setter
    def webhook_payload(self, webhook_payload: "str"):
        """Sets the webhook_payload of this WebhookActionMutable.

        The (possibly) templated payload body, which is POSTed to the webhookUrl. 

        :param webhook_payload: The webhook_payload of this WebhookActionMutable.
        :type: str
        """
        self._attrs["webhookPayload"] = webhook_payload

    @property
    def webhook_url(self) -> "str":
        """ Gets the webhook_url of this WebhookActionMutable.
        Only HTTPS is allowed. 
        """
        return self._attrs.get("webhookUrl")

    @webhook_url.setter
    def webhook_url(self, webhook_url: "str"):
        """Sets the webhook_url of this WebhookActionMutable.

        Only HTTPS is allowed. 

        :param webhook_url: The webhook_url of this WebhookActionMutable.
        :type: str
        """
        self._attrs["webhookUrl"] = webhook_url

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}
