import json
import pretty_errors
from pprint import pprint
from db import execute_query, INSER_CAMPAING_QUERY, INSERT_EMAILS_QUERY


def load_test_payload(filepath: str):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data


def dump_output_payload(output_filename: str, optput_payload: list | dict):
    with open(output_filename, "w") as f:
        json.dump(optput_payload, f)
    return True


def create_payload_for_db(input_payload: list | dict):

    result = list()
    for item in input_payload:

        campaign_insert_payload = {
            "campaign_id": item["id"],
            "name": item["name"],
            "owner_email": item["ownerEmail"],
            "from_email": item["emailAccount"],
            "to_emails": item["emailAccounts"],
            "time_created": item["created"],
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

        execute_query(INSER_CAMPAING_QUERY, campaign_insert_payload)

        # if len(campaign_insert_payload["to_emails"]) > 0:

        #     for email in campaign_insert_payload["to_emails"]:
        #         emails_insert_payload = {
        #             "email": email,
        #             "time_created": campaign_insert_payload["time_created"],
        #             "campaign_id": campaign_insert_payload["campaign_id"],
        #         }
        #         execute_query(INSERT_EMAILS_QUERY, emails_insert_payload)

        result.append(campaign_insert_payload)
    return result


def prepare_emais_payload(input_payload):
    ...


if __name__ == "__main__":
    test_payload = load_test_payload("reply_input_payload.json")
    # pprint(test_payload)
    result = create_payload_for_db(test_payload)

    dump_output_payload("repy_result_payload.json", result)
