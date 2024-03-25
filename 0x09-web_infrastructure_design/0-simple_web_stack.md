# Simple Web Stack

## Description

This ia a simple web infrastructure that hosts a website that is recheable via `www.foobar.com`. There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server.

## About the Infrastructure

* What is a server?
  - Servers are physical machines, virtual machines or softwares(computer programs) that serve or provide functionality to other programs or devices called "clients". Servers can provide various functionalities such as sharing data among multiple clients or performing computations for a client.

  - A computer can function as a server, and a server can be a computer, both of them being built up with hardware and software. However, the main difference between these two is the capacity and computer power servers have. In other words, servers are computers on steroids with faster processing capacity. They are usually stored in data centers racks (stacks of servers piled one on top of each other).

* What is the role of the domain name?
  - A domain name is a human-readable address that serves as a reference to a specific IP address on the internet. It's used to identify and locate websites. The role of a domain name is to provide a memorable and recognizable name for internet users to access websites without needing to remember the numerical IP address associated with the server hosting the website.

* What type of DNS record `www` is in `www.foobar.com`?
  - The "www" in `www.foobar.com` typically represents a subdomain, and it is commonly associated with a DNS record called a CNAME (Canonical Name) record. This record type is used to alias one domain name to another, allowing the website to be reached using the prefix "`www`."

* What is the role of the web server?
  - The web server is responsible for serving web content to users who request it via their web browsers. It processes incoming requests, retrieves the necessary files (such as HTML, CSS, JavaScript, images, etc.) from storage, and sends them back to the user's browser for display.

* What is the role of the application server?
  - The application server hosts and executes the application logic or business logic of a web application. It processes user inputs, interacts with databases, performs computations, and generates dynamic content that the web server then delivers to the user.

* What is the role of the database?
  - The database stores and manages the structured data used by the web application. It provides a way to organize, retrieve, update, and manage data efficiently. The database is crucial for storing user information, application data, and other relevant information needed by the application.

* What is the server using to communicate with the computer of the user requesting the website?
  - The server communicates with the user's computer over the internet using the HTTP (Hypertext Transfer Protocol) or its secure version, HTTPS. These protocols define the rules for how web servers and web browsers communicate and exchange data.

## Issues with the Infrastructure

* Single Point Of Failure (SPOF)
  - A single point of failure occurs when a component within a system has the potential to cause the entire system to fail if it malfunctions. In the described infrastructure, if any critical component such as the web server or database server fails, it could lead to downtime for the entire website.

* Downtime when maintenance needed
  - During maintenance activities, such as deploying new code or updating server configurations, services often need to be restarted or taken offline temporarily. This can result in downtime, where the website is inaccessible to users, leading to a negative impact on user experience and potentially business revenue.

* Scalability limitations
  - If the infrastructure cannot handle sudden spikes in incoming traffic efficiently, it indicates scalability limitations. Without proper scalability measures in place, such as load balancing, auto-scaling, or distributed architectures, the website may become slow or unavailable during periods of high traffic, hindering user experience and potentially causing loss of opportunities or revenue.
