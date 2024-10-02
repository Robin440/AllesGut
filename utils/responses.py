from rest_framework.response import Response
from rest_framework import status


def HTTP_200(data) -> Response:
    if isinstance(data, dict) is False:
        data = {"data": data}
    return Response(data, status=status.HTTP_200_OK)


def HTTP_201(data) -> Response:
    if isinstance(data, dict) is False:
        data = {"data": data}
    return Response(data, status=status.HTTP_201_CREATED)


def HTTP_202(data) -> Response:
    if isinstance(data, dict) is False:
        data = {"data": data}
    return Response(data, status=status.HTTP_202_ACCEPTED)


def HTTP_204(data) -> Response:
    if isinstance(data, dict) is False:
        data = {"data": data}
    return Response(data, status=status.HTTP_204_NO_CONTENT)


def HTTP_400(data) -> Response:
    if isinstance(data, dict) is False:
        data = {"message": data}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


def HTTP_401(data="You don't have permission to perform this action.") -> Response:
    if isinstance(data, dict) is False:
        data = {"message": data}
    return Response(data, status=status.HTTP_401_UNAUTHORIZED)


def HTTP_403(data) -> Response:
    if isinstance(data, dict) is False:
        data = {"message": data}
    return Response(data, status=status.HTTP_403_FORBIDDEN)


def HTTP_404(data) -> Response:
    if isinstance(data, dict) is False:
        data = {"message": data}
    return Response(data, status=status.HTTP_404_NOT_FOUND)


def HTTP_307(data) -> Response:
    if isinstance(data, dict) is False:
        data = {'data':data}
    return Response(data, status=status.HTTP_307_TEMPORARY_REDIRECT)


def HTTP_408(data) -> Response:
    if isinstance(data, dict) is False:
        data = {'error':data}
    return Response(data, status=status.HTTP_408_REQUEST_TIMEOUT)