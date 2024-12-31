import openreview


def get_venue_id():
    return "NeurIPS.cc/2024/Conference"


def get_client():
    client = openreview.api.OpenReviewClient(
        baseurl='https://api2.openreview.net',
        username="dotan.dicastro@gmail.com",
        password="shira1936"
    )
    return client


def get_all_venues():
    # API V2
    client = get_client()

    venues = client.get_group(id='venues').members
    for i, venue in enumerate(venues):
        if venue.startswith('NeurIPS'):
            print(f"{i} => {venue}")


def get_all_notes():
    # API V2
    client = get_client()
    venue_id = get_venue_id()
    notes = client.get_all_notes(invitation=f"{venue_id}/-/Submission")
    print(notes)


if __name__ == "__main__":
    # get_all_venues()
    get_all_notes()
