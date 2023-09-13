# Fanout Exchange

**Fanout** Exchange is an even simpler, but slightly less popular way of routing in *RabbitMQ*. This type of `exchange` sends messages
to all queues subscribed to it, ignoring any arguments of the message.

At the same time, if the queue listens to several consumers, messages will also be distributed among them.

## Example

```python linenums="1"
{!> docs_src/rabbit/subscription/fanout.py !}
```

### Consumer Announcement

To begin with, we announced our **Fanout** exchange and several queues that will listen to it:

```python linenums="7" hl_lines="1"
{!> docs_src/rabbit/subscription/fanout.py [ln:7-10]!}
```

Then we signed up several consumers using the advertised queues to the `exchange` we created

```python linenums="12" hl_lines="1 5 9"
{!> docs_src/rabbit/subscription/fanout.py [ln:12-22]!}
```

!!! note
    `handler1` and `handler2` are subscribed to the same `exchange` using the same queue:
    within a single service, this does not make a sense, since messages will come to these handlers in turn.
    Here we emulate the work of several consumers and load balancing between them.

### Message distribution

Now the distribution of messages between these consumers will look like this:

```python linenums="26"
{!> docs_src/rabbit/subscription/fanout.py [ln:26]!}
```

Message `1` will be sent to `handler1` and `handler3`, because they listen to `exchange` using different queues

---

```python linenums="27"
{!> docs_src/rabbit/subscription/fanout.py [ln:27]!}
```

Message `2` will be sent to `handler2` and `handler3`, because `handler2` listens to `exchange` using the same queue as `handler1`

---

```python linenums="28"
{!> docs_src/rabbit/subscription/fanout.py [ln:28]!}
```

Message `3` will be sent to `handler1` and `handler3`

---

```python linenums="29"
{!> docs_src/rabbit/subscription/fanout.py [ln:29]!}
```

Message `4` will be sent to `handler3` and `handler3`

---

!!! note
    When sending messages to **Fanout** exchange, it makes no sense to specify the arguments `queue` or `routing_key`, because they will be ignored