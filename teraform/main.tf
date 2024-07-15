terraform {
  required_providers {
    zitadel = {
      source  = "zitadel/zitadel"
      version = "1.3.0"
    }
  }
}

provider "zitadel" {
  domain           = "auth.samipsolutions.fi"
  insecure         = "true"
  port             = "443"
  token = "token.json"
}


resource "zitadel_org" "org" {
  name = "tmi"
}

resource "zitadel_human_user" "default" {
  org_id             = zitadel_org.org.id
  user_name          = "sm"
  first_name         = "Skyler"
  last_name          = "Mäntysaari"
  email              = "sm@samipsolutions.fi"
  initial_password   = "Password1!"
}
