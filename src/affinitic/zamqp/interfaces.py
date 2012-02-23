# -*- coding: utf-8 -*-
"""
affinitic.zamqp

Licensed under the GPL license, see LICENCE.txt for more details.

Copyright by Affinitic sprl
Copyright by University of Jyväskylä
"""
from zope.interface import Interface, Attribute
from zope.component.interfaces import IObjectEvent


class IBrokerConnection(Interface):
    """
    AMQP Broker connection to an AMQP server via a specific virtual host
    """

    hostname = Attribute('The hostname where the broker is located')

    port = Attribute('The port where the broker is running (default: 5672)')

    userid = Attribute('The user id to access the broker')

    password = Attribute("The user's password to access the broker")

    virtual_host = Attribute('The virtual host id')


class IBeforeBrokerConnectEvent(Interface):
    """
    En event tiggered once before all connections are connected at the
    first time. This won't be triggered for reconnections.
    """


class ISerializer(Interface):
    """
    A named serializer serializes and de-serializes message bodies.

    The convention is to register all serializers twice: once by their nick
    name and once by their content-type. E.g. PickleSerializer is registered as
    both as "pickle" and as "application/x-python-serialize".
    """

    content_type = Attribute("Content-type for serialized content")

    def serialize(body):
        """Return serialized body"""

    def deserialize(body):
        """return de-serialized body"""


class IConsumer(Interface):
    """
    A Consumer receive messages sent to a queue via an exchange
    """

    connection_id = Attribute('The connection id where the queue is/will be registered')

    queue = Attribute('Name of the queue')

    exchange = Attribute('Name of the exchange the queue binds to')

    exchange_type = Attribute('')

    routing_key = Attribute('')

    auto_delete = Attribute('')

    marker = Attribute("Return the interface related to the message")


class IConsumingRequest(Interface):
    """
    A request marker interface for consuming requests
    """

class IMessage(Interface):
    """
    """

class IMessageArrivedEvent(IObjectEvent):
    """
    Event fired when a new message has arrived
    """

class IPublisher(Interface):
    """
    A Publisher send message to a queue via an exchange
    """

    connection_id = Attribute('The BrokerConnection id where the queue is/will be registered')


class IErrorHandler(Interface):
    """
    Error handler for a specific exchange
    """

    def __call__(message, error, traceback):
        """
        Do something with the error and the traceback that we got while consuming message
        """
