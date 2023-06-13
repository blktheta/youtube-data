from prefect import flow, task
from prefect.blocks.system import String

string_block = String.load("demo-block")

@task
def test1():
    msg = string_block.value
    return(msg)

@flow
def demo2():
    demo_number = 2
    return(demo_number)

@flow
def demo1():
    sub_flow_msg = demo2()
    task_msg = test1()
    new_msg = task_msg + str(sub_flow_msg)
    print(new_msg)


if __name__ == "__main__":
    demo1()
