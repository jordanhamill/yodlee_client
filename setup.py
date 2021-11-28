# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "yodlee"
VERSION = "1.0.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Yodlee Core APIs",
    author_email="developer@yodlee.com",
    url="",
    keywords=["Swagger", "Yodlee Core APIs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available &lt;a href&#x3D;\&quot;https://developer.yodlee.com/java-sdk-overview \&quot;&gt;here&lt;/a&gt;. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/Overview\&quot;&gt;Yodlee API v1.1 - Overview&lt;/a&gt;.&lt;br&gt;&lt;br&gt;You will have to set the header before making the API call. The following headers apply to all the APIs:&lt;ul&gt;&lt;li&gt;Authorization: This header holds the access token&lt;/li&gt; &lt;li&gt; Api-Version: 1.1&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Note&lt;/b&gt;: If there are any API-specific headers, they are mentioned explicitly in the respective API&#39;s description.  # noqa: E501
    """
)
