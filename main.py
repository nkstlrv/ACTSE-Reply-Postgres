import json
import pretty_errors
from pprint import pprint
import db


def load_test_payload(filepath: str):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data


def dump_output_payload(output_filename: str, optput_payload: list | dict):
    with open(output_filename, "w") as f:
        json.dump(optput_payload, f)
    return True


def create_campaign_payload_for_db(input_payload: list | dict):

    result = list()
    for item in input_payload:

        campaign_insert_payload = {
            "campaign_id": item["id"],
            "name": item["name"],
            "owner_email": item["ownerEmail"],
            "from_email": item["emailAccount"],
            "to_emails": item["emailAccounts"],
            "time_campaign_created": item["created"],
            "status": item["status"],
            "delivers_count": item["deliveriesCount"],
            "opens_count": item["opensCount"],
            "replies_count": item["repliesCount"],
            "bounces_count": item["bouncesCount"],
            "opt_outs_count": item["optOutsCount"],
            "out_of_office_count": item["outOfOfficeCount"],
            "people_count": item["peopleCount"],
            "people_finished": item["peopleFinished"],
            "people_active": item["peopleActive"],
            "people_paused": item["peoplePaused"],

        }

        db.execute_query(db.INSER_CAMPAING_QUERY, campaign_insert_payload)

        # if len(campaign_insert_payload["to_emails"]) > 0:

        #     for email in campaign_insert_payload["to_emails"]:
        #         emails_insert_payload = {
        #             "email": email,
        #             "campaign_id": campaign_insert_payload["campaign_id"],
        #         }
        #         execute_query(INSERT_EMAILS_QUERY, emails_insert_payload)

        result.append(campaign_insert_payload)
    return result


def create_emails_payload_for_db(input_payload):
    result = list()

    for item in input_payload:
        for email in item["to_emails"]:
            result.append(
                {
                    "email": email,
                    "campaign_id": item["campaign_id"]
                }
            )
    return result

def insert_emails_to_db(emails: list):
    for email in email:
        db.execute_query(db.INSERT_EMAILS_QUERY, email)



if __name__ == "__main__":
    test_payload = load_test_payload("reply_input_payload.json")

    campaigns = create_campaign_payload_for_db(test_payload)
    emails = create_emails_payload_for_db(campaigns)
