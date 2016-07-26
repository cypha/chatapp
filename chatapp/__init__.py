from views import EchoSession
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.registry import Registry
from pyramid_jinja2 import _get_or_build_default_environment #?#?#?

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from pyramid_beaker import session_factory_from_settings


registry = Registry()

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    session_factory = session_factory_from_settings(settings)

    authn_policy = AuthTktAuthenticationPolicy(secret='s0secret')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(
        settings=settings,
#        root_factory='chatapp.security.RootFactory',
        authentication_policy=authn_policy,
        authorization_policy=authz_policy,
        session_factory=session_factory,
    )
    jinja_env = _get_or_build_default_environment(config.registry)

    config.add_route('home', '/')
    config.add_sockjs_route('chat-service', session=EchoSession)
    config.add_route('broadcast', '/broadcast')


    config.scan()
    return config.make_wsgi_app()

