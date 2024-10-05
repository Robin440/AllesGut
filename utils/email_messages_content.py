

# from core.settings.base import UI_DOMAIN_URL
from core.settings import EMAIL_SENDER
from django.conf import settings

UI_DOMAIN_URL=f'{settings.NGROK_URL}/api/verify/'


DEFAULT_NOTIFICATION_FROM_EMAIL = EMAIL_SENDER


def email_content(identifier, data):
    """
    This function for render mail content dynamically.
    :param identifier: mail identifier
    :param data: data for mail
    :return: mail content
    """

    # Fetching verification code from data which is from api.

    verification_code = data.get("verification_code")

    # Email content with identifiers.
    mail_content = {
        "registration": {
    "subject": f"Verification code to signup: {data.get('verification_code')} | AllesGUT",
    "from": [
        DEFAULT_NOTIFICATION_FROM_EMAIL,
    ],
    "body": {
        "title": "Activate Your Account",
        "paragraph_1": (
            f"Hi {data.get('name')},\n\n"
            "Just one more step away to access your AllesGUT account. "
            "Click the button below to verify your email and complete the registration process. "
            "Here is your OTP: {data.get('verification_code')}"
        ),
        "cta_button": {
            "text": "Verify Your Email",
            "link": "{domain}?identifier=registration&verification_token={token}&uuid={uuid}".format(
                domain=UI_DOMAIN_URL,
                token=data.get("token"),
                uuid=data.get("uuid"),
            ),
        },
        "verification_code": {
            "code": f"{data.get('verification_code')}"
        },
        "paragraph_2": (
            "This verification code is valid for the next 15 minutes. "
            "If you did not initiate this request, please ignore this email.\n\n"
            "Thank you for choosing AllesGUT."
        ),
    },
    "required_fields": ["token", "uuid", "verification_code"],
},

        "change_email": {
            "subject": f"Verification code to change email: {data.get('verification_code')} | VegaStack",
            "from": [
                DEFAULT_NOTIFICATION_FROM_EMAIL,
            ],
            "roles": ["ws_owner", "ws_admin", "ws_member", "ws_billing_manager"],
            "body": {
                "title": "Email for change email.",
                "paragraph_1": "here is your otp {{data.get('verification_code')}}",
                "cta_button": {"text": "Link", "link": "<LINK>"},
                "verification_code": {"code": f"{data.get('verification_code')}"},
                "paragraph_2": "<paragraph 2>",
            },
        },
        "password_reset": {
            "subject": f"Verification code to password reset: {data.get('verification_code')} | VegaStack",
            "from": [
                DEFAULT_NOTIFICATION_FROM_EMAIL,
            ],
            "roles": ["ws_owner", "ws_admin", "ws_member", "ws_billing_manager"],
            "body": {
                "title": "Email for reset password.",
                "paragraph_1": "<paragraph 1>",
                "cta_button": {"text": "Link", "link": "<LINK>"},
                "verification_code": {"code": f"{data.get('verification_code')}"},
                "paragraph_2": "<paragraph 2>",
            },
        },
        "resend_verification": {
    "subject": f"Verification code: {data.get('verification_code')} | AllesGUT",
    "from": [
        DEFAULT_NOTIFICATION_FROM_EMAIL,
    ],
    "body": {
        "title": "Verify your account",
        "paragraph_1": (
            f"Hi {data.get('name')},\n\n"
            "We noticed that you requested to resend the verification code for your account registration. "
            "Please use the code below to verify your email and complete the registration process."
        ),
        "cta_button": {
            "text": "Verify Now",
            "link": "<LINK>"  # Add the actual link for verification here
        },
        "verification_code": {
            "code": f"{data.get('verification_code')}"
        },
        "paragraph_2": (
            "This verification code is valid for the next 15 minutes. If you didn't request this, please ignore this email.\n\n"
            "Thank you for choosing AllesGUT."
        ),
    },


        },
        "change_ownership": {
            "subject": f"Verification code to change ownership: {data.get('verification_code')} | VegaStack",
            "from": [
                DEFAULT_NOTIFICATION_FROM_EMAIL,
            ],
            "roles": ["ws_owner", "ws_admin", "ws_member", "ws_billing_manager"],
            "body": {
                "title": "Email to change ownership.",
                "paragraph_1": "<paragraph 1>",
                "cta_button": {"text": "Link", "link": "<LINK>"},
                "verification_code": {"code": f"{data.get('verification_code')}"},
                "paragraph_2": "<paragraph 2>",
            },
        },
        "invite_workspace": {
            "subject": "Link for invite workspace: VegaStack",
            "from": [
                DEFAULT_NOTIFICATION_FROM_EMAIL,
            ],
            "roles": ["ws_owner", "ws_admin", "ws_member", "ws_billing_manager"],
            "body": {
                "title": "Email to invite to workspace.",
                "paragraph_1": "<paragraph 1>",
                "cta_button": {"text": "Link", "link": "<LINK>"},
                "verification_code": {"code": f"{data.get('verification_code')}"},
                "paragraph_2": "<paragraph 2>",
            },
        },
        "change_ownership_ws_admin": {
            "subject": "Link for accept workspace ownership: VegaStack",
            "from": [
                DEFAULT_NOTIFICATION_FROM_EMAIL,
            ],
            "roles": ["ws_owner", "ws_admin", "ws_member", "ws_billing_manager"],
            "body": {
                "title": "Email to accept ownership.",
                "paragraph_1": "<paragraph 1>",
                "cta_button": {"text": "Link", "link": "<LINK>"},
                "verification_code": {"code": f"{data.get('verification_code')}"},
                "paragraph_2": "<paragraph 2>",
            },
        },
        "account_activated": {
            "subject": "Account Activated",
            "from": [
                DEFAULT_NOTIFICATION_FROM_EMAIL,
            ],
            "roles": ["ws_owner", "ws_admin", "ws_member", "ws_billing_manager"],
            "body": {
                "title": "Your account has been activated.",
                "paragraph_1": "<paragraph 1>",
                "cta_button": {"text": "Link", "link": "<LINK>"},
                "verification_code": {"code": f"{data.get('verification_code')}"},
                "paragraph_2": "<paragraph 2>",
            },
        },
    }

    try:
        content = mail_content[identifier]
    except Exception as exc:
        raise ValueError(f"please add this {identifier} in email content. exc: {exc}") from exc

    # Validation for required fields.
    # Here we check the verification code , uuid and token from data.
    for field in content.get("required_fields", []):
        if field not in data:
            raise ValueError(f"please add this {field} in email data.")

    return content
