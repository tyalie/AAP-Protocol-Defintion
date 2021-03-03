meta:
  id: aap
  title: Apple Accessory Protocol
  endian: be
  bit-endian: be
doc: |
  The AAP (Apple Accessory Protocol) is a L2CAP based protocol used on all Apple Headphones 
  to retrieve their state, apply settings and do other cool and magical stuff.

  A popular feature of the AAP is it's ability to retrieve the charge state of the
  headphones. Something that Apple doesn't expose using the popular standards for doing
  this.
  
  Other interesting gems in the protocol, is their ability to do real time in-ear detection,
  retrieve the apple pairing magic key and configure the headphones to your liking.
seq:
  - id: msg_type
    type: u1
  - id: unknown
    contents: [0x00]
  - id: service_id 
    type: u1 
  - id: body
    size-eos: true
    type:
      switch-on: msg_type
      cases:
        0x00: connect
        0x01: connect_response
        0x04: command
types:
  connect:
    doc: Initial package by master
    seq:
      - id: major
        type: u2
      - id: minor
        type: u2
      - id: features
        size-eos: true

  connect_response:
    doc: The initial package by the slave
    seq:
      - id: status
        type: u2
      - id: major
        type: u2
      - id: minor
        type: u2
      - id: features
        size-eos: true
  
  command:
    doc: The relevant exchange in the AAP protocol

