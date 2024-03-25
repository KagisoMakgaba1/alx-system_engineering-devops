# Distributed Web Infrastructure

## Specifics of the Infrastructure

* Additional elements
1. 2 servers:
   - Adding multiple servers allows for redundancy and load distribution, reducing the risk of downtime due to hardware failures or maintenance.
2. 1 web server (Nginx):
   - Nginx is a high-performance web server and reverse proxy that can handle large amounts of concurrent connections efficiently. It's chosen for its scalability, speed, and ability to serve static content quickly.
3. 1 application server:
   - The application server hosts the application logic, handling dynamic content generation, user authentication, and business logic processing.
4. 1 load-balancer (HAproxy):
   - The load balancer distributes incoming web traffic across multiple servers to optimize resource utilization and ensure high availability. HAproxy is a reliable and efficient choice for this purpose.
5. 1 set of application files (your code base):
   - The application files contain the source code, configuration files, and assets required to run the web application.
6. 1 database (MySQL):
   - MySQL is a popular relational database management system chosen for its reliability, performance, and scalability. It stores and manages the application's data.

* Distribution algorithm for the load balancer (HAproxy):
  - HAproxy can be configured with various distribution algorithms, such as round-robin, least connections, or source IP hashing. The chosen algorithm dictates how incoming requests are distributed among the backend servers. For example, round-robin distributes requests evenly in a sequential order.

* Active-Active vs. Active-Passive setup:
  - In an Active-Active setup, both servers actively handle incoming requests simultaneously, sharing the load. In contrast, an Active-Passive setup involves one server (active) handling requests while the other server (passive) remains on standby, ready to take over if the active server fails.

* Database Primary-Replica (Master-Slave) cluster:
  - In a Primary-Replica cluster, also known as Master-Slave replication, the primary node (master) handles write operations and replicates data changes to one or more replica nodes (slaves). The replica nodes serve read-only queries and act as backups. This setup improves fault tolerance, scalability, and data redundancy.

* Difference between Primary and Replica nodes in regard to the application:
  - The primary node handles write operations, such as inserting, updating, or deleting data, while replica nodes serve read-only queries. From the application's perspective, write operations are directed to the primary node, ensuring data consistency and integrity, while read operations can be distributed across both primary and replica nodes to improve performance.

## Issues with the Infrastructure

1. Single Point of Failure (SPOF):
   - The load balancer itself can become a single point of failure. If it fails, it can disrupt the flow of traffic to the backend servers, causing downtime for the website.

2. Security issues (no firewall, no HTTPS):
   - Without a firewall, the servers are vulnerable to unauthorized access and attacks. Additionally, the absence of HTTPS encryption leaves data transmitted between the server and clients susceptible to interception and manipulation.

3. No monitoring:
   - Without proper monitoring tools and practices in place, it's challenging to detect and address performance issues, security breaches, or other potential problems proactively. Monitoring is essential for ensuring the stability, security, and optimal performance of the infrastructure.
