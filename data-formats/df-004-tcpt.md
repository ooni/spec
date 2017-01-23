# TCPTest data format

Data Format Version: 0.2.0

This specifies the data format for tests that are based on
`ooni.templates.tcpt.TCPTest`.

## Specification

```
{
    "sent": [
        "The list of the payloads of the sent data segments."
    ]
    "received": [
        "The list of the payloads of the received data segments."
    ]
}
```

## Example output

```
{
    "bucket_date": "2015-12-01",
    "data_format_version": "0.2.0",
    "id": "f116e9a4-a648-48c8-b3b7-cca7bd84d069",
    "input": null,
    "options": [],
    "probe_asn": "AS786",
    "probe_cc": "GB",
    "probe_ip": "127.0.0.1",
    "report_filename": "2015-12-01/20151201T072512Z-GB-AS786-http_invalid_request_line-ZXjsOzoy3gl0f71b35et9kLZsTkc3W1yLYMHSLVLN6buJvnXveywSBM24C2YPtfv-0.1.0-probe.json",
    "report_id": "ZXjsOzoy3gl0f71b35et9kLZsTkc3W1yLYMHSLVLN6buJvnXveywSBM24C2YPtfv",
    "software_name": "ooniprobe",
    "software_version": "1.3.1",
    "test_helpers": {
        "backend": "213.138.109.232"
    },
    "backend_version": "1.1.4",
    "input_hashes": [],
    "probe_city": null,
    "test_keys": {
        "received": [
            "53LC / HTTP/1.1\n\r",
            "",
            "dNnLP MHIdC s5vst k7Ir2\n\r",
            "yWoBwUKUnlMfZQ1BDFIHJsLAU9PNKUVOzOJ1s7BdXKlhAnALegIOkvEsq8QCHNKqFoMk5ndpSa3bE99hIVXZSK7hCGa6wk770C9WJoL7VLYDeGRYWEhoYF2eg8PERFK4CGYXuuCLkr0ScT3esnj66ypgzpuP85PpCSERP5qc0DNYzHF4edM9RcDxttfMU0X5HyQ0EzKCMX4dcKlB6DLianESEKFKE3VwRht2cwUdLs6IXG5fsUBLEiJUQEHzFENpr40dPvcnk1KoTc4UZr5EP9JlNJ9f7fx6Ps6m2QzxyXkVT8UjPYbx2Rk6EO27nfd21iKtzZyZzUhyHxVQtLS58hzeQumCwAMdOi5FmwiDG6vFS1THTODJdwovw7V0CsaXvFwkJmBagWVvRR3zWQ9o509BnK9bxvBIo5cgFdyBlVHSH3Bbq0kXyarVAoQjaOo0C8Tb8lr5Ug7FFelGnBmdKNmNQj1QmmiobrcUMY22JKdxp81Z0R1AoyjLjeJQ7NNlhpbM6REiHladSmVmgBPChjjFQJn2TGOmSAIQJAvnsREpdMyuRemTA5Vb0QMIUmEVvpIKV8HOhBaniz389ftxglIizaOF3pacUIBycUwLermpolNatVn6BbDSCNJGCwil8NVUBtfKQqTlEgQk1zo3LNfryrKEd5M4PBdOzqIFHb0zhsY8NsSy7geXOZfMnNRNfu0dsMDchiLYHzQD0qPg2heEsJ3w8usyH462eqUcNF5qNOt47tC53rnbChT8Tjktr55LrJQhvKg8QRqWg2HuTnM4eMxSjdF8iCUzxEhDHkoxah5v6iQPmRE7qCUxf2Jwyi404MLX0gGvoawukkrEiVlhcHrQo3yrnAqIRx7mYhp9izzmWw62e35xzpFD3rxhAlrLTBr3bJQPBXvMzkAY62UHt1pAQPCaDojEo1WrHKnb8TMsNUS8u5yYumvbuxsLSJFWIjkrqf2G6rm1aVo95jxx9Uvx665eJ9tWRAT6rD4A1QoXVg34m20ywW1n3voP / HTTP/1.1\n\r"
        ],
        "sent": [
            "53LC / HTTP/1.1\n\r",
            "GET / HTTP/g8z\n\r",
            "dNnLP MHIdC s5vst k7Ir2\n\r",
            "yWoBwUKUnlMfZQ1BDFIHJsLAU9PNKUVOzOJ1s7BdXKlhAnALegIOkvEsq8QCHNKqFoMk5ndpSa3bE99hIVXZSK7hCGa6wk770C9WJoL7VLYDeGRYWEhoYF2eg8PERFK4CGYXuuCLkr0ScT3esnj66ypgzpuP85PpCSERP5qc0DNYzHF4edM9RcDxttfMU0X5HyQ0EzKCMX4dcKlB6DLianESEKFKE3VwRht2cwUdLs6IXG5fsUBLEiJUQEHzFENpr40dPvcnk1KoTc4UZr5EP9JlNJ9f7fx6Ps6m2QzxyXkVT8UjPYbx2Rk6EO27nfd21iKtzZyZzUhyHxVQtLS58hzeQumCwAMdOi5FmwiDG6vFS1THTODJdwovw7V0CsaXvFwkJmBagWVvRR3zWQ9o509BnK9bxvBIo5cgFdyBlVHSH3Bbq0kXyarVAoQjaOo0C8Tb8lr5Ug7FFelGnBmdKNmNQj1QmmiobrcUMY22JKdxp81Z0R1AoyjLjeJQ7NNlhpbM6REiHladSmVmgBPChjjFQJn2TGOmSAIQJAvnsREpdMyuRemTA5Vb0QMIUmEVvpIKV8HOhBaniz389ftxglIizaOF3pacUIBycUwLermpolNatVn6BbDSCNJGCwil8NVUBtfKQqTlEgQk1zo3LNfryrKEd5M4PBdOzqIFHb0zhsY8NsSy7geXOZfMnNRNfu0dsMDchiLYHzQD0qPg2heEsJ3w8usyH462eqUcNF5qNOt47tC53rnbChT8Tjktr55LrJQhvKg8QRqWg2HuTnM4eMxSjdF8iCUzxEhDHkoxah5v6iQPmRE7qCUxf2Jwyi404MLX0gGvoawukkrEiVlhcHrQo3yrnAqIRx7mYhp9izzmWw62e35xzpFD3rxhAlrLTBr3bJQPBXvMzkAY62UHt1pAQPCaDojEo1WrHKnb8TMsNUS8u5yYumvbuxsLSJFWIjkrqf2G6rm1aVo95jxx9Uvx665eJ9tWRAT6rD4A1QoXVg34m20ywW1n3voP / HTTP/1.1\n\r"
        ],
        "tampering": true
    },
    "test_name": "http_invalid_request_line",
    "test_runtime": 5.7580039501,
    "test_start_time": "2015-12-01 07:25:12",
    "test_version": "0.2"
}
```
