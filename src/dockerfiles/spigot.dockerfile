FROM openjdk:8

ARG REV=1.14.4
ARG EULA=true

WORKDIR /download

RUN curl "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar" -o BuildTools.jar && \
    java -jar BuildTools.jar --rev ${REV} && \
    mv ./spigot-${REV}.jar ./spigot.jar

RUN echo "eula=${EULA}" > /download/eula.txt

FROM gcr.io/distroless/java:8

WORKDIR /app

COPY --from=0 /download /app

CMD [ "/app/spigot.jar" ]
