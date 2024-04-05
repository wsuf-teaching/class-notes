# HTTP

> To test the example endpoints in httpserver.py, you can follow the guide [here](../frontend1/test_server_setup.md).
> For this version of the server, you will need to install both `flask` and `flask_basicauth` with pip.

The HTTP (Hypertext Transfer Protocol) is the foundation of data communication for the World Wide Web.
It is a protocol used by web browsers and servers to communicate and transfer hypertext documents,
such as HTML documents. Here's an overview of how it works:

HTTP operates on a client-server model in a request-response cycle. 
The client, typically a web browser, sends HTTP requests to the server, which hosts the web pages or resources 
requested by the client and responds with an HTTP response containing the requested resource or an error message.

All resources on the web, such as web pages, images, or files, are identified by Uniform Resource Identifiers (URIs). 
URIs are used in HTTP requests to specify the location of the requested resource. More specifically, these identifiers
are called URLs (Uniform Resource Locators) if used on the internet.

HTTP is a stateless protocol, meaning that each request from the client to the server is independent
and not reliant on previous requests. This simplifies the implementation of web servers and improves scalability but
requires additional mechanisms such as cookies or session management for maintaining state between requests.

HTTPS (HTTP Secure) is an extension of HTTP that uses encryption (typically SSL/TLS) to secure
the communication between the client and server, providing confidentiality 
and integrity of data transferred over the network.

## Methods

HTTP defines several methods (also known as verbs) that indicate the desired
action to be performed on the resource identified by the URI. Common HTTP methods include:
* GET: Requests a representation of the specified resource.
* POST: Submits data to be processed to the specified resource.
* PUT: Uploads a representation of the specified resource.
* DELETE: Deletes the specified resource.
* HEAD: Requests the headers of the specified resource without the body.
* OPTIONS: Requests permitted communication options for a given URL or server.

PUT or POST?
By the RFC 2616 definitions:
The POST method is used to request that the origin server accept the entity enclosed in the request 
as a new subordinate of the resource identified by the Request-URI in the Request-Line.

The PUT method requests that the enclosed entity be stored under the supplied Request-URI. 
If the Request-URI refers to an already existing resource, the enclosed entity SHOULD be 
considered as a modified version of the one residing on the origin server. 
If the Request-URI does not point to an existing resource, and that URI is capable of 
being defined as a new resource by the requesting user agent, the origin server can create the resource with that URI.

## Headers

HTTP requests and responses contain headers, which provide additional information about the request or response.
Headers include metadata such as content type, content length, caching directives, and more.

## Status Codes

HTTP responses include status codes that indicate the result of the request.
Typically, the "hundreds" define a status code "group" or "type".
* 1xx - Informational: These status codes indicate that the request has been received and understood,
and the server is continuing with the process.
* 2xx - Success: These status codes indicate that the request was successfully received, understood, and accepted.
* 3xx - Redirection: These status codes indicate that further action needs to be taken by the client to complete the request.
* 4xx - Client Error: These status codes indicate that there was a problem with the client's request.
* 5xx - Server Error: These status codes indicate that there was an error on the server while processing the request.

## Ways of sending and requesting data

### URL parameters
The values are passed directly in the URL path.

```http://localhost:5000/url_params/John/25```

Parameters are directly visible in the URL, making it easy to share and bookmark.
Limited in the amount and type of data that can be sent. URLs have length limitations, and certain characters may need to be encoded.
Security concern: sensitive data should not be included in the URL, as it can be easily visible and potentially logged.

### Query parameters
The values are passed as part of the URL query string.

```http://localhost:5000/query_params?name=Jane&age=30```

Parameters are directly visible in the URL, making it easy to share and bookmark.
More flexible than URL parameters as the order can vary, and parameters can be optional.
Can be easily manipulated and tested using browser address bars or tools like cURL.
Less visible than URL parameters, as they are appended to the URL.
Not suitable for sending large amounts of data, as it can become cluttered and harder to manage.
Security concern: similar to URL parameters, query parameters are visible in the URL and should not be used for sensitive data without encryption.

### JSON body
The values are sent as part of the request body in JSON format.

Supports sending structured data in a flexible format.
Suitable for complex data structures and larger amounts of data.
Can include nested objects and arrays, providing better organization and readability.
Encourages the use of standard data formats (JSON), making it easier to integrate with various platforms and languages.
Can include headers for additional information, such as content type or authentication tokens.
Requires more effort to implement on both the client and server sides compared to URL or query parameters.
Not as human-readable as URL or query parameters when inspecting requests directly.
Can not be saved as links or bookmarks.
Increased bandwidth consumption due to additional overhead from JSON formatting.
May not be directly visible or editable in some tools, requiring specialized software for testing and debugging.

