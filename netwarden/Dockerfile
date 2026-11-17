# Two stages: build a wheel, then install it into a small image that runs as a normal user.
FROM python:3.13-slim AS build
WORKDIR /src
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir build && python -m build --wheel

FROM python:3.13-slim
RUN useradd --create-home --uid 10001 warden
COPY --from=build /src/dist/*.whl /tmp/
RUN pip install --no-cache-dir /tmp/*.whl && rm /tmp/*.whl
USER warden
WORKDIR /home/warden
ENTRYPOINT ["netwarden"]
CMD ["--help"]
