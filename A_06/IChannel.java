package util;

import java.io.Closeable;
import java.io.IOException;

public interface IChannel extends Closeable {
	public void printLine(String message) throws IOException;

	public void printLine(byte[] message) throws IOException;

	public String readLine() throws IOException;

	public byte[] readLineBytes() throws IOException;

	@Override
	public void close() throws IOException;
}
