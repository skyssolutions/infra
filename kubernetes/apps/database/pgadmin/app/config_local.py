AUTHENTICATION_SOURCES = ['internal','oauth2']
OAUTH2_AUTO_CREATE_USER = True
MASTER_PASSWORD_REQUIRED = False

OAUTH2_CONFIG = [{
  'OAUTH2_NAME' : 'Zitadel',
  'OAUTH2_DISPLAY_NAME' : 'IdP',
  'OAUTH2_CLIENT_ID' : '${PGADMIN_OAUTH_CLIENT_ID}',
  'OAUTH2_CLIENT_SECRET' : '${PGADMIN_OAUTH_SECRET}',
  'OAUTH2_TOKEN_URL' : 'https://auth.${SECRET_DOMAIN_2}/oauth/v2/token',
  'OAUTH2_AUTHORIZATION_URL' : 'https://auth.${SECRET_DOMAIN_2}/oauth/v2/authorize',
  'OAUTH2_API_BASE_URL' : 'https://auth.${SECRET_DOMAIN_2}/',
  'OAUTH2_USERINFO_ENDPOINT' : 'https://auth.${SECRET_DOMAIN_2}/oidc/v1/userinfo',
  'OAUTH2_SERVER_METADATA_URL' : 'https://auth.${SECRET_DOMAIN_2}/.well-known/openid-configuration',
  'OAUTH2_SCOPE' : 'openid email profile groups',
  'OAUTH2_ICON' : 'fa-openid',
  'OAUTH2_BUTTON_COLOR' : '#2db1fd'
}]
