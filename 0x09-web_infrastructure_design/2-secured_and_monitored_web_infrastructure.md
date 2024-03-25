# Secured and Monitored Web Infrastruture

## Specifics of the Infrastructure

* Additional elements
1. 3 firewalls:
   - Firewalls are added to enforce security policies and control incoming and outgoing network traffic. They act as a barrier between a trusted internal network and untrusted external networks, helping to prevent unauthorized access, malicious attacks, and data breaches.
2. 1 SSL certificate to serve `www.foobar.com` over HTTPS:
   - Serving traffic over HTTPS encrypts the data transmitted between the server and clients, ensuring confidentiality, integrity, and authentication. An SSL certificate is required to establish a secure connection and validate the authenticity of the server to the clients.
3. 3 monitoring clients (data collector for Sumo Logic or other monitoring services):
   - Monitoring is essential for detecting and diagnosing issues, optimizing performance, and ensuring the reliability and security of the infrastructure. Monitoring clients, such as data collectors for Sumo Logic or similar services, gather data from various sources within the infrastructure for analysis and visualization.

* Why firewalls are necessary:
   - Firewalls provide an additional layer of security by inspecting and filtering incoming and outgoing traffic based on predefined rules. They help protect against unauthorized access, malware, and other cyber threats.

* Why traffic is served over HTTPS:
   - Serving traffic over HTTPS encrypts sensitive data, such as login credentials, personal information, and financial transactions, preventing eavesdropping and tampering by malicious actors. It also helps build trust with users by demonstrating a commitment to security and privacy.

* Purpose of monitoring:
   - Monitoring is used to track the performance, availability, and security of the infrastructure and applications. It helps identify issues, troubleshoot problems, optimize resources, and ensure compliance with service-level agreements (SLAs).

* How monitoring tools collect data:
   - Monitoring tools collect data from various sources, including server logs, performance metrics, network traffic, application logs, and system events. This data is collected, aggregated, and analyzed to generate insights, alerts, and reports.

* Monitoring web server QPS:
   - To monitor the web server's queries per second (QPS), you can use monitoring tools to track metrics related to incoming HTTP requests. This includes monitoring metrics such as request count, request rate, response time, and error rate. By analyzing these metrics over time, you can identify trends, anomalies, and performance bottlenecks.

## Issues with the Infrastructure

1. Terminating SSL at the load balancer level:
   - Terminating SSL at the load balancer means that decrypted traffic is forwarded to the backend servers. This exposes the internal network to potential security risks if the communication between the load balancer and backend servers is not adequately secured.

2. Having only one MySQL server capable of accepting writes:
   - Having a single MySQL server capable of accepting writes introduces a single point of failure for write operations. If the MySQL server fails, it can result in data loss, downtime, and service disruptions.

3. Having servers with all the same components (database, web server, and application server):
   - Having identical server configurations across the infrastructure can lead to uniform vulnerabilities and dependencies. If a critical vulnerability is discovered or a component fails, it can affect all servers simultaneously, increasing the risk of widespread downtime and security breaches. Introducing diversity in server configurations can mitigate this risk.
