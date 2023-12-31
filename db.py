from pprint import pprint
import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSOWRD = "postgres"
DB_HOST = "localhost"
DB_PORT = 5432


def execute_query(query: str = None, query_params: dict = None) -> bool | str | None:
    if query is not None:
        try:
            connection = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSOWRD,
                host=DB_HOST,
                port=DB_PORT,
            )

            coursor = connection.cursor()

            coursor.execute(query, query_params)
            print("EXECUTING QUERY")

            if "select" in query.lower():
                response = coursor.fetchall()
                return response
            return True

        except psycopg2.Error as e:
            print("Error connecting to the database:", e)

        finally:
            connection.commit()
            coursor.close()
            connection.close()
    return


INSER_CAMPAING_QUERY = """
        INSERT INTO reply_io_campaigns 
            (
            campaign_id,
            name,
            owner_email,
            from_email,
            to_emails,
            time_campaign_created,
            status,
            delivers_count,
            opens_count,
            replies_count,
            bounces_count,
            opt_outs_count,
            out_of_office_count,
            people_count,
            people_finished,
            people_active,
            people_paused
            )
            VALUES
            (%(campaign_id)s, %(name)s, %(owner_email)s, %(from_email)s, %(to_emails)s,
            %(time_campaign_created)s, %(status)s, %(delivers_count)s, %(opens_count)s,
            %(replies_count)s, %(bounces_count)s, %(opt_outs_count)s, %(out_of_office_count)s,
            %(people_count)s, %(people_finished)s, %(people_active)s, %(people_paused)s)

            ON CONFLICT (campaign_id)
            DO NOTHING;
"""


INSERT_EMAILS_QUERY = """
    INSERT INTO reply_io_emails
        (
            email,
            campaign_id
        )
    VALUES
        (
            %(email)s,
            %(campaign_id)s
        )
"""


if __name__ == "__main__":
    pprint(execute_query("SELECT * FROM reply_io_campaigns"))
    pprint(execute_query("SELECT * FROM reply_io_emails"))



# INSERT_EMAILS_QUERY = """
#     INSERT INTO reply_io_emails
#         (
#             email,
#             campaign_id
#         )
#     VALUES
#         (
#             %(email)s,
#             %(campaign_id)s
#         )
#     ON CONFLICT (email)
#     DO UPDATE
#     SET time_db_entry = NOW();
# """