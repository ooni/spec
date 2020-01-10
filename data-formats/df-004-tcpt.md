# TCPTest Data Format

This document describes the keys with `test_keys` that all experiments
sending and receiving data using TCP template SHOULD populate, possibly
using directly the specific template code. See this directory's
[README](README.md) for the basic concepts.

## Specification

```JSON
{
    "received": [],
    "sent": []
}
```

- `received` (`[]MaybeBinaryData`): list of data received. See the
definition of `MaybeBinaryData` in `df-001-httpt.md`, which in
the common case boils down to an UTF-8 string.

- `sent`: like `received` but contains sent data.

## Example

In the following example we've omitted all the keys that are
not relevant to the TCP data format:

```JSON
{
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
    }
}
```
