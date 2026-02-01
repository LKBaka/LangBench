Module Module1

Function Fib(ByVal n As Integer) As Long
    If n <= 1 Then
        Return n
    End If
    Return Fib(n - 1) + Fib(n - 2)
End Function

Sub Main()
    Dim n As Integer = 30
    Dim result As Long = Fib(n)
    Console.WriteLine(result)
End Sub
End Module
