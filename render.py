#!/usr/local/bin/python2.7
from jinja2 import Environment, FileSystemLoader, select_autoescape


def read_file_without_title(filename):
    """
    Takes filename of markdown as input and returns the file contents as a
    utf-8 encoded string after stripping out the title
    """
    file_lines = open(filename).readlines()

    while True:
        line = file_lines[0].decode('utf-8').strip()

        # If the line is empty or begins with a `# ` denoting a h1 md header
        if line == '' or line[:2] == '# ':
            # Remove the first line
            file_lines.pop(0)
        else:
            break

    # At this point, file_lines is stripped of the title.
    # Return the utf string
    return "".join(file_lines)


def render():
    """
    Given the necessary markdown files that are maintained on Github in the
    `lnd` repo, renders the guides with Jekyll header.
    """

    # Load the Jekyll header from the `templates` dir
    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('base.md')

    # Read INSTALL.md and output guides/installation.md
    installation_guide = template.render(
        title='Installation',
        permalink=None,
        content=read_file_without_title('INSTALL.md'),
        footer=open('templates/installation_footer.md').read(),
    ).encode('utf-8')
    installation_output = 'guides/installation.md'
    with open(installation_output, "wb") as file_out:
        file_out.write(installation_guide)
    print "Rendered {}".format(installation_output)

    # Read DOCKER-README.md and output guides/docker.md
    docker_guide = template.render(
        title='Working with LND and Docker',
        permalink=None,
        content=read_file_without_title('DOCKER-README.md'),
    ).encode('utf-8')
    docker_output = 'guides/docker.md'
    with open(docker_output, "wb") as file_out:
        file_out.write(docker_guide)
    print "Rendered {}".format(docker_output)

    # Read python.md and output guides/python-grpc.md
    python_grpc_guide = template.render(
        title='How to write a Python gRPC client for the Lightning Network Daemon',
        permalink=None,
        content=read_file_without_title('python.md'),
    ).encode('utf-8')
    python_grpc_output = 'guides/python-grpc.md'
    with open(python_grpc_output, "wb") as file_out:
        file_out.write(python_grpc_guide)
    print "Rendered {}".format(python_grpc_output)

    # Read javascript.md and output guides/javascript-grpc.md
    javascript_grpc_guide = template.render(
        title='How to write a Javascript gRPC client for the Lightning Network Daemon',
        permalink=None,
        content=read_file_without_title('javascript.md'),
    ).encode('utf-8')
    javascript_grpc_output = 'guides/javascript-grpc.md'
    with open(javascript_grpc_output, "wb") as file_out:
        file_out.write(javascript_grpc_guide)
    print "Rendered {}".format(javascript_grpc_output)


if __name__ == '__main__':
    render()
