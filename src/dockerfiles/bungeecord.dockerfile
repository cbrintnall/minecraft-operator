FROM openjdk:8

WORKDIR /download

ARG BUILD_NUM=1421

RUN curl -o bungee.jar https://ci.md-5.net/job/BungeeCord/${BUILD_NUM}/artifact/bootstrap/target/BungeeCord.jar

FROM gcr.io/distroless/java:8

WORKDIR /app

COPY --from=0 /download/bungee.jar /app/bungee.jar

CMD [ "/app/bungee.jar" ]
