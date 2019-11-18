# selfcaffeinate

## Description

Python module to prevent macOS system sleep using the `caffeinate(1)` command

### Introduction to `caffeinate(1)`
macOS users can prevent system sleep using the `caffeinate` like so:

```console
$ caffeinate sh -c "echo sleeping; sleep 60; echo done"
sleeping
done
$
```

Or hold a power management assertion on an existing process:
```console
$ pgrep long-running-process
555
$ caffeinate -w 555 && echo "done"
done
```

This module allows `caffeinate` to be used programmatically from Python code to prevent system sleep, without having to run the command externally.

## Example usage:

```python
def main():
    print("Self caffeinating")
    SLEEP_PERIOD = 60
    sc = SelfCaffeinate()
    for i in range(0, 60):
        print("Sleeping {}".format(SLEEP_PERIOD))
        time.sleep(SLEEP_PERIOD)
```

Or use the `with` pattern:

```python
def main():
    print("Self caffeinating")
    SLEEP_PERIOD = 60
    with SelfCaffeinate()
      for i in range(0, 60):
          print("Sleeping {}".format(SLEEP_PERIOD))
          time.sleep(SLEEP_PERIOD)
```

The default path to macOS's `caffeinate` should work, but if you have an alternate path, you can specify that:

```python
def main():
    print("Self caffeinating")
    SLEEP_PERIOD = 60
    sc = SelfCaffeinate(caffeinate_path="/path/to/my/weird/caffeinate")
    for i in range(0, 60):
        print("Sleeping {}".format(SLEEP_PERIOD))
        time.sleep(SLEEP_PERIOD)
```
