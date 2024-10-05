GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
RESET = "\033[0m"
print(f"{YELLOW_BOLD}LOADING GET MODULE FROM 'get_details.py'{RESET}")


# models import
from member.models import Member,MemberImage

def get_member(user):
    """Get a member from the database based on the user ID."""
    try:
        member = Member.objects.get(user = user)
        return member
    except Member.DoesNotExist:
        return None

def get_member_image(member):
    """Get a member image from the database based on the member ID."""
    try:
        member_image = MemberImage.objects.get(member = member)
        return member_image
    except MemberImage.DoesNotExist:
        return None



print(f"{GREEN_BOLD}****************************** get module loaded successfully ******************************{RESET}")

