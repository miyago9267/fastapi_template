from faker import Faker
from project_name.models.people import People, Job

fake = Faker(['zh_TW'])

def generate_people(size: int = 1) -> list:
    """Generate a list of people"""
    people_list = []
    for _ in range(size):
        ssnid = fake.unique.ssn()
        gender = fake.random_element(elements=('男','女'))
        name = fake.name()
        id_hash = fake.sha256(ssnid.encode('utf-8')).hexdigest()
        social_credits = fake.random_int(min=0, max=100)
        people_list.append(
            People(id=ssnid, gender=gender, name=name, hash=id_hash, credits=social_credits)
        )
    return people_list


def generate_job(size: int=1) -> list:
    """Generate a list of job with people_list"""
    job_list = []
    for _ in range(size):
        name = fake.job()
        people_list = generate_people(5)
        type_int = fake.random_int(min=0, max=1)
        id_hash = fake.sha256(name.encode('utf-8')).hexdigest()

        job_list.append(
            Job(name=name, people_list=people_list, type=type_int, hash=id_hash)
        )
    return job_list

if __name__ == "__main__":
    print(generate_job(3))
