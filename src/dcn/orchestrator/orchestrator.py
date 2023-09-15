import docker

def build_image(input_name):
    client = docker.from_env()
    IMG_NAME = 'virtual_plc_'
    image = client.images.build(path=".", tag=IMG_NAME + input_name)
    return image

def start_container(img, srv, object, input, output, time_w):
    client = docker.from_env()
    container = client.containers.run(img, f'python3 dcn.py {srv} {object} {input} {output} {time_w}', detach=True)
    return container