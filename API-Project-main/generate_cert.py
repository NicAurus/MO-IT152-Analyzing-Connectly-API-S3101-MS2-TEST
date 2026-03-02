import trustme

ca = trustme.CA()
server_cert = ca.issue_cert("localhost")

ca.cert_pem.write_to_path("ca.pem")
server_cert.cert_chain_pems[0].write_to_path("cert.pem")
server_cert.private_key_pem.write_to_path("key.pem")

print("Certificates generated.")