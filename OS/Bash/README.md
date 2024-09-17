# Heredoc
When writing shell scripts you may be in a situation where you need to pass a multiline block of text or code to an interactive command, such as tee , cat, or sftp .

In Bash and other shells like Zsh, a Here document (Heredoc) is a type of redirection that allows you to pass multiple lines of input to a command.

The syntax of writing HereDoc takes the following form:
```
[COMMAND] <<[-] 'DELIMITER'
  HERE-DOCUMENT
DELIMITER
```

## Basic Heredoc Examples
In this section, we will look at some basic examples of how to use heredoc.

Heredoc is most often used in combination with the cat command .

In the following example, we are passing two lines of text containing an environment variable and a command to cat using a here document.

```
cat << EOF
The current working directory is: $PWD
You are logged in as: $(whoami)
EOF
```
As you can see from the output below, both the variable and the command output are substituted:
```
The current working directory is: /home/linuxize
You are logged in as: linuxize
```

Let’s see what will happen if we enclose the delimiter in single or double quotes.
```
cat <<- "EOF"
The current working directory is: $PWD
You are logged in as: $(whoami)
EOF
```
You can notice that when the delimiter is quoted no parameter expansion and command substitution is done by the shell.
```
The current working directory is: $PWD
You are logged in as: $(whoami)
```

If you are using a heredoc inside a statement or loop, use the <<- redirection operation that allows you to indent your code.
```
if true; then
    cat <<- EOF
    Line with a leading tab.
    EOF
fi
```
output
```
Line with a leading tab.
```

Instead of displaying the output on the screen you can redirect it to a file using the >, >> operators.
```
cat << EOF > file.txt
The current working directory is: $PWD
You are logged in as: $(whoami)
EOF
```
If the file.txt doesn’t exist it will be created. When using > the file will be overwritten, while the >> will append the output to the file.

The heredoc input can also be piped. In the following example the sed command will replace all instances of the l character with e:
```
cat <<'EOF' |  sed 's/l/e/g'
Hello
World
EOF
```
output:
```

Heeeo
Wored
```
To write the piped data to a file:
```
cat <<'EOF' |  sed 's/l/e/g' > file.txt
Hello
World
EOF
```